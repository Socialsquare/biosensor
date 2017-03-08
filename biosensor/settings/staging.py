import os
import dj_database_url

from .base import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SITE_ID = 1
DOMAIN = 'biosensor-staging.herokuapp.com'
EMAIL_DOMAIN = 'staging.biosensor.dk'
ALLOWED_HOSTS = [DOMAIN, ]

DATABASES = {
    'default': dj_database_url.config()
}
# DATABASES['default']['ENGINE'] = 'django_postgrespool'
DATABASE_POOL_ARGS = {
    'max_overflow': 10,
    'pool_size': 5,
    'recycle': 300
}

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEFAULT_FROM_EMAIL = 'Biosensor (staging) <info@{0}>'.format(EMAIL_DOMAIN)
SERVER_EMAIL = 'Biosensor (staging) <alerts@{0}>'.format(EMAIL_DOMAIN)

ADMINS = (
    ('Kraen', 'kraen+biosensor-staging@socialsquare.dk', ),
)
SITE_ADMIN_EMAIL = 'pemye@bio.dtu.dk'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['SMTP_SERVER']
EMAIL_HOST_USER = os.environ['SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['SMTP_PASSWORD']
EMAIL_PORT = os.environ['SMTP_PORT']
EMAIL_USE_TLS = True
