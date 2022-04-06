from django import template

register = template.Library()

@register.filter(name='get_color')
def color(value,arg):
    if value < arg:
        return True
    else:
        return False