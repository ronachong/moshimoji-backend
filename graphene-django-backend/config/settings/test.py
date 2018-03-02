from .base import *
from config.settings.helpers import Secrets

SECRETS_DIR = '/home/rona/projects/moshimoji/docker/secrets/dev'
SECRETS = Secrets(SECRETS_DIR).dict
SECRET_KEY = SECRETS['DJANGO']

# if I understand correctly, test handlers will prefix db name with TEST to
# avoid collision with actual db data
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

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
