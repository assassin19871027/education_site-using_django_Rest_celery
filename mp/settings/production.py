from __future__ import absolute_import

from .base import *



DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'manuelcepeda',
        'PASSWORD': 'ingasdfg',
        'HOST': 'localhost',
        'PORT': '',
    }
}