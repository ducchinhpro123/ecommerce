from django import template

from product.models import Book

register = template.Library()


@register.filter
def is_book(product):
    if isinstance(product, Book):
        print("is book")
        return True
    else:
        print("is not book")
        return False
