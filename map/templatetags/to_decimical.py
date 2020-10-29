from django import template

register = template.Library()

@register.filter
def to_decimical(value):
    return value.replace(",",".")
