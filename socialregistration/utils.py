import uuid
from django.conf import settings

USE_HTTPS = bool(getattr(settings, 'SOCIALREGISTRATION_USE_HTTPS', False))


def generate_username(user, profile, client):
    """
    Default function to generate usernames using the built in `uuid` library.
    """
    return str(uuid.uuid4())[:30]


def is_https():
    """
    Check if the site is using HTTPS. This is controlled with
    ``SOCIALREGISTRATION_USE_HTTPS`` setting.
    """
    return USE_HTTPS
