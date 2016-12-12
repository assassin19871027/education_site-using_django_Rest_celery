

from .base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.db",
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'