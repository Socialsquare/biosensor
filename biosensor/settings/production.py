import os
import dj_database_url

from .base import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SITE_ID = 1
DOMAIN = 'biosensor.dk'
ALLOWED_HOSTS = [
    DOMAIN,
    'www.' + DOMAIN,
]

DATABASES = {
    'default': dj_database_url.config()
}
DATABASES['default']['ENGINE'] = 'django_postgrespool'
DATABASE_POOL_ARGS = {
    'max_overflow': 10,
    'pool_size': 5,
    'recycle': 300
}

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEFAULT_FROM_EMAIL = 'Biosensor <info@{0}>'.format(DOMAIN)
SERVER_EMAIL = 'Biosensor <alerts@{0}>'.format(DOMAIN)

ADMINS = (
    ('Pernille', 'pemye@bio.dtu.dk', ),
)
SITE_ADMIN_EMAIL = 'pemye@bio.dtu.dk'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['SMTP_SERVER']
# EMAIL_HOST_USER = os.environ['SMTP_LOGIN']
# EMAIL_HOST_PASSWORD = os.environ['SMTP_PASSWORD']
EMAIL_PORT = os.environ['SMTP_PORT']
EMAIL_USE_TLS = False
