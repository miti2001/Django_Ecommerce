from django import template

register = template.Library()

@register.filter
def get_id_dict(content):
    return content['id']