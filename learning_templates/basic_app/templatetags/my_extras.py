from django import template

register = template.Library()

# @register.filter(name = 'cut12')

@register.simple_tag
def cut12(value, arg):
    """
    This cuts out all values of "arg" from the string
    """

    return value.relace(arg,"")


# register.filter('cut',cut)
