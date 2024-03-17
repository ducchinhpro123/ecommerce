from django import template

from product.models import Book

register = template.Library()


@register.filter
def is_book(product):
    return isinstance(product, Book)
