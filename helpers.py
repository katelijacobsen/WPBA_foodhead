from flask import request, make_response
from functools import wraps # use decorator so the function knows automatically not to cache
import re # Regex
import regex
import config

#_____NO CACHE_____###################################
def no_cache(view):
    @wraps(view)
    def no_cache_view(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    return no_cache_view
###################################_____NO CACHE_____#

    
    
#_____VALIDATION FOR USER_____###############
############### FIRST NAME
def validate_user_first_name():
    user_first_name = request.form.get("user_first_name").strip()
    if not re.match(regex.REGEX_USER_NAME, user_first_name):
        raise Exception (f"____whoops user_first_name")
    
    return user_first_name

############### LAST NAEM
def validate_user_last_name():
    user_last_name = request.form.get("user_last_name").strip()
    if not re.match(regex.REGEX_USER_NAME, user_last_name):
        raise Exception(f"____whoops user_last_name")
    
    return user_last_name

############### USERNAME
def validate_user_username():
    user_username = request.form.get("user_username").strip()
    if not re.match(regex.REGEX_USER_NAME, user_username):
        raise Exception(f"____whoops user_username")
    
    return user_username

############### PASSWORD
def validate_user_password():
    user_password = request.form.get("user_password", "").strip()
    # if user didn't add password
    if not user_password:
        raise Exception("INVALID_PASSWORD user_password")
    
    #if password does not live up to the expectations
    if not re.match(regex.REGEX_USER_PASSWORD, user_password):
        raise Exception(f"Password must be at least {regex.USER_PASSWORD_MIN} characters long")
    
    return user_password

############### EMAIL
def validate_user_email():
    user_email = request.form.get("user_email", "").strip() # use strip() to avoid spacing from left- and right side of the input
    if not re.match(regex.REGEX_USER_EMAIL, user_email):
        raise Exception("INVALID_EMAIL user_email")
    return user_email

############### PHONE NUMBER
def validate_user_phonenumber():
    user_phonenumber = request.form.get("user_phonenumber", "").strip()
    if not re.match(regex.REGEX_USER_PHONE, user_phonenumber):
        return Exception("INVALID_PHONENUMBER user_phonenumber")
###############_____VALIDATION FOR USER_____#


#_____VALIDATION FOR CREATING RECIPE_____###################
def validate_recipe_title():
    recipe_title = request.form.get("recipe_title", "").strip()
    if not re.match(regex.REGEX_RECIPE_TITLE, recipe_title):
        raise Exception("foodhead recipe_title")
    return recipe_title


def validate_recipe_description():
    recipe_description = request.form.get("recipe_description", "").strip()
    if not re.match( regex.REGEX_RECIPE_DESCRIPTION ,recipe_description):
        raise Exception("foodheadn recipe_description")
    return recipe_description


def validation_recipe_servings():
    recipe_servings = request.form.get("recipe_servings", "").strip()
    if not re.match(regex.REGEX_RECIPE_SERVINGS, recipe_servings):
        raise Exception("foodhead recipe_servings")
    return recipe_servings

def validation_recipe_instructions():
    recipe_instruction = request.form.get("recipe_instruction", "").strip()
    if not re.match(regex.REGEX_RECIPE_INSTRUCTIONS, recipe_instruction):
        raise Exception("foodhead recipe_instruction")
    return recipe_instruction
###################_____VALIDATION FOR CREATING RECIPE_____#