import os
import dj_database_url

from .base import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SITE_ID = 1
DOMAIN = 'biosensor-staging.herokuapp.com'
ALLOWED_HOSTS = [DOMAIN, ]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

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

DEFAULT_FROM_EMAIL = 'Info <info@{0}>'.format(DOMAIN)
SERVER_EMAIL = 'Alerts <alerts@{0}>'.format(DOMAIN)

ADMINS = (
    ('Simon', 'simon.carstensen+biosensor-staging-heroku@socialsquare.dk',),
)
SITE_ADMIN_EMAIL = 'pemye@bio.dtu.dk'
