import json

from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.data import JsonLexer


def json_field_pp(d):
    response = json.dumps(d, sort_keys=True, indent=2)
    formatter = HtmlFormatter(style='colorful')
    response = highlight(response, JsonLexer(), formatter)
    style = "<style>" + formatter.get_style_defs() + "</style><br>"
    return mark_safe(style + response)
