from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
@stringfilter
def convert_email(email):
	return email.replace('@', ' # ').replace('.', '_')
