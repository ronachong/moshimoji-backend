"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

def get_config_module():
    if not os.path.isfile('/.dockerenv'):
        return 'local'
    return 'stage' if int(os.environ['STAGE']) else 'production'

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings.{}".format(get_config_module())
)

application = get_wsgi_application()
