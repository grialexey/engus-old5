from django.template import Library, Node
from django.template.defaultfilters import stringfilter
import re

register = Library()


def list_items(value):
    """
    Turns paragraphs delineated with newline characters into
    list items wrapped in <li> and </li> HTML tags.
    """
    items = re.split(r'[\r\n]+', value)
    items = ['<li>%s</li>' % p.strip() for p in items]
    return '\n'.join(items)
paragraphs = stringfilter(list_items)

register.filter(paragraphs)