from django import template
from django.template import loader

register = template.Library()

class LoginNode(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        return loader.get_template('member_content/login.html').render(context.flatten())

@register.tag
def print_login_form(parser, token):
    return LoginNode()