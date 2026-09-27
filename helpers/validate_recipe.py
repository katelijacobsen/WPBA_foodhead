from flask import request
import re
import regex
from helpers.validation import ValidationError, _text, _length, _number

#_____VALIDATION FOR RECIPES_____#######################
def validate_recipe_title():
    return _text("recipe_title", regex.REGEX_RECIPE_TITLE,
                 f"Use {regex.RECIPE_TITLE_MIN}–{regex.RECIPE_TITLE_MAX} characters")


def validate_recipe_description():
    return _length("recipe_description", regex.RECIPE_DESCRIPTION_MIN, regex.RECIPE_DESCRIPTION_MAX,
                   f"Use {regex.RECIPE_DESCRIPTION_MIN}–{regex.RECIPE_DESCRIPTION_MAX} characters")


def validate_recipe_servings():
    return _number("recipe_servings", regex.RECIPE_SERVINGS_MIN, regex.RECIPE_SERVINGS_MAX,
                   f"Enter {regex.RECIPE_SERVINGS_MIN}–{regex.RECIPE_SERVINGS_MAX} servings")


def validate_recipe_minutes(field):
    return _number(field, regex.RECIPE_MINUTES_MIN, regex.RECIPE_MINUTES_MAX,
                   f"Enter {regex.RECIPE_MINUTES_MIN}–{regex.RECIPE_MINUTES_MAX} minutes")


def validate_ingridients():
    names = request.form.getlist("ingridient_name")
    amounts = request.form.getlist("ingridient_amount")
    units = request.form.getlist("ingridient_unit")

    rows = []
    for name, amount, unit in zip(names, amounts, units):
        name, amount, unit = name.strip(), amount.strip().replace(",", "."), unit.strip()
        if not name and not amount:
            continue  # ignore rows the user left empty
        if not 1 <= len(name) <= regex.INGRIDIENT_NAME_MAX:
            raise ValidationError("ingridients", f"Give every ingredient a name of up to {regex.INGRIDIENT_NAME_MAX} characters")
        if not re.match(regex.REGEX_INGRIDIENT_AMOUNT, amount) or len(amount) > regex.INGRIDIENT_AMOUNT_MAX:
            raise ValidationError("ingridients", f"Give “{name}” an amount as a number, like 250 or 1.5")
        if unit not in regex.INGRIDIENT_UNITS:
            raise ValidationError("ingridients", f"Choose a unit for “{name}” from the list")
        rows.append((name, amount, unit))

    if not rows:
        raise ValidationError("ingridients", "Add at least one ingredient")
    if len(rows) > regex.RECIPE_INGRIDIENTS_MAX:
        raise ValidationError("ingridients", f"Use at most {regex.RECIPE_INGRIDIENTS_MAX} ingredients")
    return rows


def validate_instructions():
    steps = [step.strip() for step in request.form.getlist("instruction") if step.strip()]
    if not steps:
        raise ValidationError("instructions", "Add at least one step")
    if len(steps) > regex.RECIPE_STEPS_MAX:
        raise ValidationError("instructions", f"Use at most {regex.RECIPE_STEPS_MAX} steps")
    for number, step in enumerate(steps, start=1):
        if not regex.INSTRUCTION_MIN <= len(step) <= regex.INSTRUCTION_MAX:
            raise ValidationError("instructions", f"Step {number} needs {regex.INSTRUCTION_MIN}–{regex.INSTRUCTION_MAX} characters")
    return steps


def image_extension(file):
    return file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""


def validate_recipe_image(required):
    file = request.files.get("recipe_file")
    if not file or not file.filename:
        if required:
            raise ValidationError("recipe_img", "Add a photo of your dish")
        return None
    if image_extension(file) not in regex.IMAGE_EXTENSIONS:
        raise ValidationError("recipe_img", "Use a PNG, JPG or WebP image")
    return file
#######################_____VALIDATION FOR RECIPES_____#