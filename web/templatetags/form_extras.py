from django import template

register = template.Library()

@register.inclusion_tag('form_field.html')
def show_form_field(field, icon=False):
    return {'field': field, 'icon': icon}


