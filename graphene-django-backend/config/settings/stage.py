from .base import *
from config.settings.helpers import Secrets

print("in stage config")

# TODO: maybe get this dir from an env var to make more secure
SECRETS_DIR = '/run/secrets/'
SECRETS = Secrets(SECRETS_DIR).dict

# TODO: change this to actual prod key later
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS['DJANGO']

DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = ['stage.moshi-moji.xyz']

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        # Misago requires PostgreSQL to run
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SECRETS['DB_NAME'],
        'USER': SECRETS['DB_USERNAME'],
        'PASSWORD': SECRETS['DB_PASSWORD'],
        'HOST': 'database',
        'PORT': 5432,
    }
}

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
