from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def is_active(context, view_name, active_class='active', **kwargs):
    request = context['request']
    resolver_match = request.resolver_match
    if resolver_match.view_name == view_name and resolver_match.kwargs == kwargs:
        return active_class
    return ''
