from django import template
from django.template import loader

register = template.Library()

class MenuNode(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        return loader.get_template('menu/menu.html').render(context.flatten())

@register.tag
def print_menu(parser, token):
    return MenuNode()