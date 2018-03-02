from .base import *

from config.settings.helpers import Secrets

print("in local/dev config")

# TODO: maybe get this dir from an env var to make more secure
SECRETS_DIR = '/home/rona/projects/moshimoji/docker/secrets/dev'
SECRETS = Secrets(SECRETS_DIR).dict

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS['DJANGO']

# A list of strings representing the host/domain names that this Django site can serve.
# If you are unsure, just enter here your domain name, eg. ['mysite.com', 'www.mysite.com']
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        # Misago requires PostgreSQL to run
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SECRETS['DB_NAME'],
        'USER': SECRETS['DB_USERNAME'],
        'PASSWORD': SECRETS['DB_PASSWORD'],
        'HOST': SECRETS['DB_ENDPOINT'],
        'PORT': 5432,
    }
}

DEBUG = env.bool('DJANGO_DEBUG', default=True)

# based on https://docs.djangoproject.com/en/1.11/topics/logging/#configuring-logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s M%(module)s P%(process)d T%(thread)d \n%(message)s\n'
        }
    },
    'handlers': {
        'console' : {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}
