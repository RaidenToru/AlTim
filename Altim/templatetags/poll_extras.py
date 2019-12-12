from django import template

register = template.Library()

@register.filter
def plus(value,arg):
    return value+arg

@register.filter
def multiply(value,arg):
    return value*arg

@register.filter
def pluswithsale3(value,arg):
    return (value+arg)*0.97

@register.filter
def pluswithsale5(value,arg):
    return (value+arg)*0.95

@register.filter
def pluswithsale7(value,arg):
    return (value+arg)*0.93

@register.filter
def pluswithsale10(value,arg):
    return (value+arg)*0.90
