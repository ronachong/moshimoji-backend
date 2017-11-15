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
