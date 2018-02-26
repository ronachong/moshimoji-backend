from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='ddhue(=qe14tlx(#dk2&x6r#ky4pk4f6tx9mvnhfdx_*7v)r6'
)


DEBUG = env.bool('DJANGO_DEBUG', default=True)


# A list of strings representing the host/domain names that this Django site can serve.
# If you are unsure, just enter here your domain name, eg. ['mysite.com', 'www.mysite.com']
ALLOWED_HOSTS = []


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
