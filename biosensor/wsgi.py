"""
WSGI config for biosensor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biosensor.settings")

ENVIRON_KEYS = ['DJANGO_ENV', 'DJANGO_SECRET_KEY', 'DATABASE_URL', 'SMTP_SERVER', 'SMTP_PORT']

def application(environ, start_response):
    # Moves environment variables from the apache config to the os.environ dict
    for k in ENVIRON_KEYS:
        os.environ[k] = environ.get(k, os.environ.get(k, ''))
    application = get_wsgi_application()
    return DjangoWhiteNoise(application)(environ, start_response)
