import os
import sys
from .base import *


SECRET_KEY = 'secret key'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += ('django_nose', )

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
     '--verbosity=2',
     '--with-yanc',
     '--cover-branches',
     '--cover-erase',
     '--cover-package=bioadmin',
     '--cover-package=biobricks',
     '--cover-package=biosensor',
     '--cover-package=content',
     '--cover-package=studentgroups',
     '--cover-package=teachers',
     'bioadmin',
     'biobricks',
     'biosensor',
     'content',
     'studentgroups',
     'teachers'
]

for arg in sys.argv:
    if arg.startswith('--tests='):
        NOSE_ARGS = [
            '--verbosity=2',
            '--stop',
            '--with-yanc',
        ]
        break

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'biosensor': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'bioadmin': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'scools': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'biosensor-tests': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
