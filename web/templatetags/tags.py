from django import template

register = template.Library()

@register.inclusion_tag('templatetags/form_field.html')
def show_form_field(field, icon=False):
    return {'field': field, 'icon': icon}

@register.inclusion_tag('templatetags/learning_resource.html')
def show_resource(resource):
    return {'resource': resource}