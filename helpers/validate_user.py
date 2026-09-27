from flask import request
import regex
from helpers.validation import ValidationError, _text

#_____VALIDATION FOR USER_____###############
NAME_MESSAGE = f"Use {regex.USER_NAME_MIN}–{regex.USER_NAME_MAX} characters"


def validate_user_first_name():
    return _text("user_first_name", regex.REGEX_USER_NAME, NAME_MESSAGE)


def validate_user_last_name():
    return _text("user_last_name", regex.REGEX_USER_NAME, NAME_MESSAGE)


def validate_user_username():
    return _text("user_username", regex.REGEX_USER_NAME, NAME_MESSAGE)


def validate_user_password():
    return _text("user_password", regex.REGEX_USER_PASSWORD,
                 f"Use {regex.USER_PASSWORD_MIN}–{regex.USER_PASSWORD_MAX} characters")


def validate_user_email():
    user_email = _text("user_email", regex.REGEX_USER_EMAIL, "Enter an email like name@example.com")
    if len(user_email) > regex.USER_EMAIL_MAX:
        raise ValidationError("user_email", f"Use at most {regex.USER_EMAIL_MAX} characters")
    return user_email


def validate_user_phone():
    return _text("user_phone", regex.REGEX_USER_PHONE,
                 f"Use {regex.USER_PHONE_MIN}–{regex.USER_PHONE_MAX} digits")


def validate_user_country_id():
    user_country_id = request.form.get("user_country_id", "").strip()
    if not user_country_id:
        raise ValidationError("user_country_id", "Choose your country")
    return user_country_id
###############_____VALIDATION FOR USER_____#