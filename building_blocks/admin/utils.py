import json

from django.utils.html import format_html_join, format_html
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


def render_attrs(attrs):
    return format_html_join(
        ' ', '{}="{}"', ((k, v) for k, v in attrs.items())
    )


def render_element(tag, children=None, attrs=None):
    attrs = attrs or {}
    if children is None:
        return format_html(
            """<{} {}>""",
            tag, render_attrs(attrs)
        )
    else:
        return format_html(
            """<{tag} {attrs}>{children}</{tag}>""",
            tag=tag, attrs=render_attrs(attrs), children=children
        )


def render_img(src, alt="", attrs=None):
    attrs = attrs or {}
    attrs['src'] = src
    if alt:
        attrs['alt'] = alt
    return render_element('img', attrs=attrs)


def render_anchor(href, children, new_tab=True, attrs=None):
    attrs = attrs or {}
    attrs['href'] = href
    if new_tab:
        attrs['target'] = '_blank'
        attrs['rel'] = 'noreferrer'
    return render_element('a', children, attrs=attrs)
