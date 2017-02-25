from jinja2 import utils


def sanitize_html(html_text):
    return utils.escape(html_text)