from django import template

register = template.Library()

@register.filter
def plus(value,arg):
    return value+arg
