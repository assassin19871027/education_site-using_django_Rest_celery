

from .base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.db",
    }
}


#send mails to console in development
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CELERY SETTINGS
BROKER_URL = "amqp://myuser:mp@localhost:5672/myvhost"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Santiago'
#CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
#CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# CELERY_EMAIL SETTINGS
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

CELERY_EMAIL_TASK_CONFIG = {
    'name': 'djcelery_email_send',
    'ignore_result': True,
}

CELERY_IMPORTS = ('djcelery_email.tasks',)