from flask import request
import re
import regex


# Knows which field failed, so the route can show the message next to that field
class ValidationError(Exception):
    def __init__(self, field, message):
        super().__init__(message)
        self.field = field
        self.message = message


## Match the text against a regex
def _text(field, pattern, message):
    value = request.form.get(field, "").strip()
    if not re.match(pattern, value):
        raise ValidationError(field, message)
    return value


## Match the length. Length instead of regex, so text with line breaks (textareas) passes
def _length(field, minimum, maximum, message):
    value = request.form.get(field, "").strip()
    if not minimum <= len(value) <= maximum:
        raise ValidationError(field, message)
    return value


## Match a whole number within a range
def _number(field, minimum, maximum, message):
    value = request.form.get(field, "").strip()
    if not re.match(regex.REGEX_WHOLE_NUMBER, value) or not minimum <= int(value) <= maximum:
        raise ValidationError(field, message)
    return int(value)


## Match the UUID
def validate_id(value):
    return bool(re.match(regex.REGEX_ID, value or ""))