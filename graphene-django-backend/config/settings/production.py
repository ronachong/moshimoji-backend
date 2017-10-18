from .base import *

# TODO: change this to actual prod key later
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='ddhue(=qe14tlx(#dk2&x6r#ky4pk4f6tx9mvnhfdx_*7v)r6'
)

DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = []
