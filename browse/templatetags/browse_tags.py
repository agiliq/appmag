from math import ceil
from django import template

register = template.Library()

@register.filter
def rounded(val):
    val = float(val)
    return ceil(val*2)
