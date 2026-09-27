from helpers import tip, validate_recipe, formatting
from flask import Flask, flash, render_template, request, g, session, redirect, url_for, abort
from flask_session import Session
from icecream import ic

import config
import regex
from config import close
from helpers import tip, validate_recipe
from helpers.cache import no_cache
from helpers.validation import ValidationError, validate_id
from api.user import user_api
import os
import time
import uuid

UPLOAD_FOLDER = "./static/uploads"

ic.configureOutput(prefix=f"________________________________|  '", includeContext=True)

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.config["MAX_CONTENT_LENGTH"] = regex.IMAGE_MAX_MB * 1000 * 1000
Session(app)

# Routes that live in their own files
app.register_blueprint(user_api)

# Every template can read the rules as {{ rules.USER_PASSWORD_MIN }}
app.jinja_env.filters.update(
    duration=formatting.duration,
    iso_duration=formatting.iso_duration,
    date_text=formatting.date_text,
    date_iso=formatting.date_iso,
)
app.jinja_env.globals["rules"] = regex


@app.before_request
def load_user():
    g.user = None
    user_id = session.get("user_id")
    # Static files (CSS, images, fonts) don't need the user, so skip the database
    if not user_id or request.endpoint == "static":
        return
    db, cursor = config.db()
    try:
        # Only the columns the templates need, never the password hash
        cursor.execute("SELECT user_id, user_username FROM users WHERE user_id = %s", (user_id,))
        g.user = cursor.fetchone()
    finally:
        close(db, cursor)


########################HELPERS#########################
def is_owner(recipe):
    return g.user is not None and recipe is not None and g.user["user_id"] == recipe["user_id"]


def deny_unless_owner(recipe):
    """Returns an error response for mixhtml requests, or None when the current user owns the recipe."""
    if not g.user:
        return tip.tip_tool("error", "Log in to change recipes"), 401
    if not recipe:
        return tip.tip_tool("error", "That recipe doesn't exist anymore"), 404
    if not is_owner(recipe):
        return tip.tip_tool("error", "You can only change your own recipes"), 403
    return None


def new_file_key(file):
    # Random name + checked extension. The user's own filename is never used on disk
    return f"{uuid.uuid4().hex}.{validate_recipe.image_extension(file)}"


def delete_upload(file_key):
    path = os.path.join(UPLOAD_FOLDER, file_key or "")
    if file_key and os.path.isfile(path):
        os.remove(path)


def read_recipe_form(require_image):
    # Same order as the fields in the form, so the first error shown is the one highest up
    return {
        "title": validate_recipe.validate_recipe_title(),
        "prep_time": validate_recipe.validate_recipe_minutes("recipe_prep_time"),
        "cook_time": validate_recipe.validate_recipe_minutes("recipe_cook_time"),
        "servings": validate_recipe.validate_recipe_servings(),
        "image": validate_recipe.validate_recipe_image(required=require_image),
        "description": validate_recipe.validate_recipe_description(),
        "ingridients": validate_recipe.validate_ingridients(),
        "instructions": validate_recipe.validate_instructions(),
    }


########################QUERIES#########################
def get_recipes(cursor):
    cursor.execute("""
        SELECT recipes.recipe_id, recipes.recipe_title, recipes.recipe_img_key,
               recipes.recipe_prep_time, recipes.recipe_cook_time, recipes.recipe_servings,
               users.user_username
        FROM recipes
        LEFT JOIN users ON users.user_id = recipes.user_id
        ORDER BY recipes.recipe_created_at DESC
    """)
    return cursor.fetchall()


def get_recipe(cursor, recipe_id):
    cursor.execute("""
        SELECT
            recipes.recipe_id,
            recipes.user_id,
            recipes.recipe_title,
            recipes.recipe_description,
            recipes.recipe_img_key,
            recipes.recipe_servings,
            recipes.recipe_prep_time,
            recipes.recipe_cook_time,
            recipes.recipe_created_at,
            users.user_username
        FROM recipes
        LEFT JOIN users ON users.user_id = recipes.user_id
        WHERE recipes.recipe_id = %s
    """, (recipe_id,))
    return cursor.fetchone()


def get_recipe_ingridients(cursor, recipe_id):
    cursor.execute("""
        SELECT ingridient_names, ingridient_amounts, ingridient_units
        FROM ingridients
        WHERE recipe_fk = %s
    """, (recipe_id,))
    return cursor.fetchall()


def get_recipe_instructions(cursor, recipe_id):
    cursor.execute("""
        SELECT instruction, instruction_step_number
        FROM instructions
        WHERE recipe_fk = %s
        ORDER BY instruction_step_number ASC
    """, (recipe_id,))
    return cursor.fetchall()


def load_recipe_details(recipe_id):
    db = cursor = None
    try:
        db, cursor = config.db()
        recipe = get_recipe(cursor, recipe_id)
        if not recipe:
            return None, [], []
        return recipe, get_recipe_ingridients(cursor, recipe_id), get_recipe_instructions(cursor, recipe_id)
    finally:
        close(db, cursor)


def get_countries(cursor):
    cursor.execute("SELECT country_id, country_name FROM countries ORDER BY country_name")
    return cursor.fetchall()


# Create and update both replace all rows. Nothing is saved before db.commit(), so it's all-or-nothing
def replace_ingridients(cursor, recipe_id, rows):
    cursor.execute("DELETE FROM ingridients WHERE recipe_fk = %s", (recipe_id,))
    cursor.executemany(
        "INSERT INTO ingridients (ingridient_id, recipe_fk, ingridient_names, ingridient_amounts, ingridient_units) VALUES (%s, %s, %s, %s, %s)",
        [(uuid.uuid4().hex, recipe_id, name, amount, unit) for name, amount, unit in rows]
    )


def replace_instructions(cursor, recipe_id, steps):
    cursor.execute("DELETE FROM instructions WHERE recipe_fk = %s", (recipe_id,))
    cursor.executemany(
        "INSERT INTO instructions (instruction_id, recipe_fk, instruction, instruction_step_number) VALUES (%s, %s, %s, %s)",
        [(uuid.uuid4().hex, recipe_id, step, number) for number, step in enumerate(steps, start=1)]
    )


########################PAGES#########################
### INDEX ###
@app.get("/")
@no_cache
def index():
    db = cursor = None
    try:
        db, cursor = config.db()
        recipes = get_recipes(cursor)
    finally:
        close(db, cursor)
    return render_template("index.html", user=g.user, recipes=recipes)


### SIGNUP ###
@app.get("/signup")
@no_cache
def signup():
    if g.user:
        return redirect(url_for("index"))
    db = cursor = None
    try:
        db, cursor = config.db()
        countries = get_countries(cursor)
    finally:
        close(db, cursor)
    return render_template("signup.html", countries=countries)


### LOGIN ###
@app.get("/login")
@no_cache
def login():
    if g.user:
        return redirect(url_for("index"))
    return render_template("login.html")


### LOGOUT ###
@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


### CREATE RECIPE ###
@app.get("/create")
@no_cache
def create_page():
    if not g.user:
        return redirect(url_for("login"))
    return render_template("create.html")


### SINGLE RECIPE ###
@app.get("/recipe/<recipe_id>")
@no_cache
def view_recipe(recipe_id):
    if not validate_id(recipe_id):
        abort(404)
    recipe, ingridients, instructions = load_recipe_details(recipe_id)
    if not recipe:
        abort(404)
    return render_template(
        "recipe.html",
        recipe=recipe,
        ingridients=ingridients,
        instructions=instructions,
        is_owner=is_owner(recipe),
    )


### EDIT RECIPE (full page, used when JavaScript is off) ###
@app.get("/recipe/<recipe_id>/edit")
@no_cache
def edit_recipe(recipe_id):
    if not g.user:
        return redirect(url_for("login"))
    if not validate_id(recipe_id):
        abort(404)
    recipe, ingridients, instructions = load_recipe_details(recipe_id)
    if not recipe:
        abort(404)
    if not is_owner(recipe):
        abort(403)
    return render_template("edit.html", recipe=recipe, ingridients=ingridients, instructions=instructions)


########################ERROR HANDLERS#########################
@app.errorhandler(413)
def file_too_large(error):
    return tip.form_error("recipe_img", f"Use an image under {regex.IMAGE_MAX_MB} MB"), 413


####################### RECIPE APIs ##########################
# User APIs (signup, login) live in api/user.py

## CREATE RECIPE
@app.post("/api-create-recipe")
def api_create_recipe():
    if not g.user:
        return tip.tip_tool("error", "Log in to share a recipe"), 401
    db = cursor = None
    try:
        form = read_recipe_form(require_image=True)
        recipe_id = uuid.uuid4().hex
        file_key = new_file_key(form["image"])

        db, cursor = config.db()
        cursor.execute("""
            INSERT INTO recipes (recipe_id, user_id, recipe_title, recipe_img_key, recipe_description,
                                 recipe_prep_time, recipe_cook_time, recipe_servings, recipe_created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (recipe_id, g.user["user_id"], form["title"], file_key, form["description"],
              form["prep_time"], form["cook_time"], form["servings"], int(time.time())))
        replace_ingridients(cursor, recipe_id, form["ingridients"])
        replace_instructions(cursor, recipe_id, form["instructions"])
        db.commit()

        # Save the file only after the database has everything
        form["image"].save(os.path.join(UPLOAD_FOLDER, file_key))

        flash("Recipe shared", "success")
        return tip.redirect_to(url_for("view_recipe", recipe_id=recipe_id))

    except ValidationError as ex:
        return tip.form_error(ex.field, ex.message), 400
    except Exception as ex:
        ic(ex)
        return tip.server_error(), 500
    finally:
        close(db, cursor)


## GET EDIT FORM (loaded into the recipe page by mix-get)
@app.get("/api-get-recipe-form/<recipe_id>")
@no_cache
def api_get_recipe_form(recipe_id):
    if not validate_id(recipe_id):
        return tip.tip_tool("error", "That recipe doesn't exist"), 404
    try:
        recipe, ingridients, instructions = load_recipe_details(recipe_id)
        denied = deny_unless_owner(recipe)
        if denied:
            return denied

        form = render_template("_recipe_form.html", recipe=recipe, ingridients=ingridients, instructions=instructions)
        # Swap the recipe for the form, then move focus to the form heading so screen readers follow along
        return (
            f'<browser mix-update="#recipe-view">{form}</browser>'
            + tip.call("focusElement", "recipe-form-heading")
        )
    except Exception as ex:
        ic(ex)
        return tip.server_error(), 500


## UPDATE RECIPE
@app.patch("/api-update-recipe/<recipe_id>")
def api_update_recipe(recipe_id):
    if not validate_id(recipe_id):
        return tip.tip_tool("error", "That recipe doesn't exist"), 404
    db = cursor = None
    try:
        db, cursor = config.db()
        recipe = get_recipe(cursor, recipe_id)
        denied = deny_unless_owner(recipe)
        if denied:
            return denied

        form = read_recipe_form(require_image=False)
        file_key = new_file_key(form["image"]) if form["image"] else recipe["recipe_img_key"]

        cursor.execute("""
            UPDATE recipes SET
                recipe_title = %s, recipe_description = %s, recipe_img_key = %s,
                recipe_servings = %s, recipe_prep_time = %s, recipe_cook_time = %s
            WHERE recipe_id = %s AND user_id = %s
        """, (form["title"], form["description"], file_key, form["servings"],
              form["prep_time"], form["cook_time"], recipe_id, g.user["user_id"]))
        replace_ingridients(cursor, recipe_id, form["ingridients"])
        replace_instructions(cursor, recipe_id, form["instructions"])
        db.commit()

        if form["image"]:
            form["image"].save(os.path.join(UPLOAD_FOLDER, file_key))
            delete_upload(recipe["recipe_img_key"])

        flash("Recipe updated", "success")
        return tip.redirect_to(url_for("view_recipe", recipe_id=recipe_id))

    except ValidationError as ex:
        return tip.form_error(ex.field, ex.message), 400
    except Exception as ex:
        ic(ex)
        return tip.server_error(), 500
    finally:
        close(db, cursor)


## DELETE RECIPE
@app.delete("/api-delete-recipe/<recipe_id>")
def api_delete_recipe(recipe_id):
    # The dialog is modal, so it must close before an error tip can be seen or announced
    close_dialog = tip.call("closeDialog", "delete-dialog")
    if not validate_id(recipe_id):
        return close_dialog + tip.tip_tool("error", "That recipe doesn't exist"), 404
    db = cursor = None
    try:
        db, cursor = config.db()
        recipe = get_recipe(cursor, recipe_id)
        denied = deny_unless_owner(recipe)
        if denied:
            html, status = denied
            return close_dialog + html, status

        # ingridients has no foreign key to recipes, so remove its rows by hand.
        # instructions and recipes_ingridients are removed by ON DELETE CASCADE.
        cursor.execute("DELETE FROM ingridients WHERE recipe_fk = %s", (recipe_id,))
        cursor.execute("DELETE FROM recipes WHERE recipe_id = %s AND user_id = %s", (recipe_id, g.user["user_id"]))
        db.commit()
        delete_upload(recipe["recipe_img_key"])

        flash(f"“{recipe['recipe_title']}” was deleted", "success")
        return tip.redirect_to(url_for("index"))

    except Exception as ex:
        ic(ex)
        return close_dialog + tip.server_error(), 500
    finally:
        close(db, cursor)