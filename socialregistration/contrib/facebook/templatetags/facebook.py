from django import template
from django.conf import settings
from socialregistration.templatetags import button
from socialregistration.utils import is_https

register = template.Library()

register.tag('facebook_button', button('socialregistration/facebook/facebook_button.html'))

@register.inclusion_tag('socialregistration/facebook_js.html')
def facebook_js():
    return {'facebook_api_key': settings.FACEBOOK_API_KEY, 'is_https': is_https()}