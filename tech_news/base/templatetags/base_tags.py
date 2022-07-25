from django import template

register = template.Library()


@register.simple_tag()
def title(data="Tech News Blog"):
    return data
