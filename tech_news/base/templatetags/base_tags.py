from django import template

from base.models import Category

register = template.Library()


@register.simple_tag()
def title(data="Tech News Blog"):
    return data


@register.inclusion_tag("base/partials/category_navbar.html")
def category_navbar():
    return {
        "category": Category.objects.filter(status=True)
    }
