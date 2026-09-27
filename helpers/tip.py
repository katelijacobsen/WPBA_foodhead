from flask import render_template
from markupsafe import escape

# How long each tip stays, in ms. None = stays until dismissed, so errors can be read at the user's own pace (WCAG 2.2.1)
TIP_TTL = {"success": 5000, "info": 8000, "error": None}


def tip_tool(status, title, message=""):
    html = render_template("_tip.html", status=status, title=title, message=message, ttl=TIP_TTL[status])
    # Remove older error tips first so repeated attempts don't pile up
    return (
        '<browser mix-remove=".toast--error"></browser>'
        f'<browser mix-after-begin="#toasts">{html}</browser>'
    )


def call(function_name, argument=""):
    # mixhtml calls window[function_name](argument)
    return f'<browser mix-function="{function_name}">{escape(argument)}</browser>'


def field_error(field_id, message):
    return (
        f'<browser mix-update="#{field_id}-error">{escape(message)}</browser>'
        + call("markInvalid", field_id)
    )


def form_error(field_id, message):
    return field_error(field_id, message) + tip_tool("error", "Check the highlighted field")


def server_error():
    return tip_tool("error", "Something went wrong on our side", "Try again in a moment.")


def redirect_to(url):
    return f'<browser mix-redirect="{escape(url)}"></browser>'