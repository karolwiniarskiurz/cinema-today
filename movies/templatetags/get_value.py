from django import template

register = template.Library()


@register.filter
def get_value(obj, key):
    try:
        return obj[key]
    except:
        return None
