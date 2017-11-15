"""
Django settings for forum project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Define placeholder gettext function
# This function will mark strings in settings visible to makemessages
# without need for Django's i18n features be initialized first.
_ = lambda x: x


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/



# Caching
# https://docs.djangoproject.com/en/1.11/topics/cache/#setting-up-the-cache

CACHES = {
    'default': {
        # Misago doesn't run well with LocMemCache in production environments
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


# Email configuration
# https://docs.djangoproject.com/en/1.11/ref/settings/#email-backend

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25


# If either of these settings is empty, Django won't attempt authentication.

EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''


# Default email address to use for various automated correspondence from the site manager(s).

DEFAULT_FROM_EMAIL = 'Forums <%s>' % EMAIL_HOST_USER


# Application definition

# Django Rest Framework
# http://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'misago.core.rest_permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'EXCEPTION_HANDLER': 'misago.core.exceptionhandler.handle_api_exception',
    'UNAUTHENTICATED_USER': 'misago.users.models.AnonymousUser',
    'URL_FORMAT_OVERRIDE': None,
}


# Misago specific settings
# https://misago.readthedocs.io/en/latest/developers/settings.html

# PostgreSQL text search configuration to use in searches
# Defaults to "simple", for list of installed configurations run "\dF" in "psql"
# Standard configs as of PostgreSQL 9.5 are: dutch, english, finnish, french,
# german, hungarian, italian, norwegian, portuguese, romanian, russian, simple,
# spanish, swedish and turkish
# Example on adding custom language can be found here: https://github.com/lemonskyjwt/plpstgrssearch

MISAGO_SEARCH_CONFIG = 'simple'


# Path to directory containing avatar galleries
# Those galleries can be loaded by running loadavatargallery command

MISAGO_AVATAR_GALLERY = os.path.join(BASE_DIR, 'avatargallery')


# Profile fields

MISAGO_PROFILE_FIELDS = [
    {
        'name': _("Personal"),
        'fields': [
            'misago.users.profilefields.default.FullNameField',
            'misago.users.profilefields.default.GenderField',
            'misago.users.profilefields.default.BioField',
            'misago.users.profilefields.default.LocationField',
        ],
    },
    {
        'name': _("Contact"),
        'fields': [
            'misago.users.profilefields.default.TwitterHandleField',
            'misago.users.profilefields.default.SkypeIdField',
            'misago.users.profilefields.default.WebsiteField',
        ],
    },
    {
        'name': _("IP address"),
        'fields': [
            'misago.users.profilefields.default.JoinIpField',
            'misago.users.profilefields.default.LastIpField',
        ],
    },
]
