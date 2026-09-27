from flask import Blueprint, flash, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from icecream import ic
import mysql.connector
import time
import uuid

import config
from helpers import tip, validate_user
from helpers.validation import ValidationError

user_api = Blueprint("user_api", __name__)


def country_exists(cursor, country_id):
    cursor.execute("SELECT 1 FROM countries WHERE country_id = %s", (country_id,))
    return cursor.fetchone() is not None


## SIGN UP
@user_api.post("/api-create-user")
def api_create_user():
    db = cursor = None
    try:
        user_username = validate_user.validate_user_username()
        user_first_name = validate_user.validate_user_first_name()
        user_last_name = validate_user.validate_user_last_name()
        user_country_id = validate_user.validate_user_country_id()
        user_email = validate_user.validate_user_email()
        user_phone = validate_user.validate_user_phone()
        user_password = validate_user.validate_user_password()

        db, cursor = config.db()
        if not country_exists(cursor, user_country_id):
            raise ValidationError("user_country_id", "Choose a country from the list")

        cursor.execute("""
            INSERT INTO users (user_id, user_username, user_first_name, user_last_name, user_email,
                               user_phone, user_country_id, user_password, user_created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (uuid.uuid4().hex, user_username, user_first_name, user_last_name, user_email,
              user_phone, user_country_id, generate_password_hash(user_password), int(time.time())))
        db.commit()

        flash("Account created. Log in to start cooking.", "success")
        return tip.redirect_to(url_for("login"))

    except ValidationError as ex:
        return tip.form_error(ex.field, ex.message), 400
    except mysql.connector.IntegrityError as ex:
        # The unique keys in the database are the final check for duplicates
        if "user_email" in ex.msg:
            return tip.form_error("user_email", "That email already has an account"), 400
        if "user_username" in ex.msg:
            return tip.form_error("user_username", "That username is taken"), 400
        ic(ex)
        return tip.server_error(), 500
    except Exception as ex:
        ic(ex)
        return tip.server_error(), 500
    finally:
        config.close(db, cursor)


## LOGIN
@user_api.post("/api-login")
def api_login():
    db = cursor = None
    try:
        user_email = validate_user.validate_user_email()
        user_password = validate_user.validate_user_password()

        db, cursor = config.db()
        cursor.execute("SELECT user_id, user_password FROM users WHERE user_email = %s", (user_email,))
        user = cursor.fetchone()

        # Same message for both cases, so nobody can find out which emails have an account
        if not user or not check_password_hash(user["user_password"], user_password):
            return tip.tip_tool("error", "Wrong email or password", "Check both and try again."), 400

        session["user_id"] = user["user_id"]
        flash("Welcome back", "success")
        return tip.redirect_to(url_for("index"))

    except ValidationError as ex:
        return tip.form_error(ex.field, ex.message), 400
    except Exception as ex:
        ic(ex)
        return tip.server_error(), 500
    finally:
        config.close(db, cursor)