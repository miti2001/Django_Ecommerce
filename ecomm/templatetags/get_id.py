from django import template

register = template.Library()

@register.filter
def get_id(row):
    return row[0]