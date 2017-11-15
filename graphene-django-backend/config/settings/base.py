"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import environ
import logging

# Build paths inside the project like this: str(ROOT_DIR.path('addn_path'))
ROOT_DIR = environ.Path(__file__) - 3 # computes to graphene-django-backend/
APPS_DIR = ROOT_DIR.path('project')

# Import environment vars in .env
# following: https://medium.com/@djstein/modern-django-part-1-project-refactor-and-meeting-the-django-settings-api-d2784efb606f
env = environ.Env() # will search for .env in projectroot

logger = logging.getLogger('django')

# This section added from an update to standards in CookieCutter Django to
# ensure no errors are encountered at runserver/migrations
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    env_file = str(ROOT_DIR.path('.env'))
    ('Loading : {}'.format(env_file))
    env.read_env(env_file)
    logger.info('CONFIG: The .env file has been loaded. See base.py for more information')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# (secret keys, allow_hosts set in local, production and test)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', False)


# Application definition
AUTH_USER_MODEL = 'misago_users.User'

AUTHENTICATION_BACKENDS = [
    'misago.users.authbackends.MisagoBackend',
]

CSRF_FAILURE_VIEW = 'misago.core.errorpages.csrf_failure'

MISAGO_CORE = (
    # Misago overrides for Django core feature
    'misago',
    'misago.users',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.postgres',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'graphene_django',
    'django_filters',
    'rest_framework',   # used by misago (and my graphql stuff)
    'corsheaders',
    'debug_toolbar',    # used by misago
    'crispy_forms',     # used by misago
    'mptt',             # used by misago
)

MISAGO_APPS = (
    'misago.admin',
    'misago.acl',
    'misago.core',
    'misago.conf',
    'misago.markup',
    'misago.legal',
    'misago.categories',
    'misago.threads',
    'misago.readtracker',
    'misago.search',
    'misago.faker',
)

LOCAL_APPS = (
    'project.gql_platform',
)

INSTALLED_APPS = MISAGO_CORE + DJANGO_APPS + THIRD_PARTY_APPS + MISAGO_APPS + LOCAL_APPS

INTERNAL_IPS = [
    '127.0.0.1'
]

LOGIN_REDIRECT_URL = 'misago:index'

LOGIN_URL = 'misago:login'

LOGOUT_URL = 'misago:logout'

MIDDLEWARE_CLASSES = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'misago.users.middleware.RealIPMiddleware',
    'misago.core.middleware.frontendcontext.FrontendContextMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'project.custom_middleware.jwt.JWTMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'misago.users.middleware.UserMiddleware',
    'misago.core.middleware.exceptionhandler.ExceptionHandlerMiddleware',
    'misago.users.middleware.OnlineTrackerMiddleware',
    'misago.admin.middleware.AdminAuthMiddleware',
    'misago.threads.middleware.UnreadThreadsCountMiddleware',
    'misago.core.middleware.threadstore.ThreadStoreMiddleware',
]

ROOT_URLCONF = 'config.urls' # ROOT_URLCONF = 'forum.urls' in original misago conf

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # os.path.join(BASE_DIR, 'theme', 'templates'), in original misago conf
            str(APPS_DIR.path('theme/templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'misago.core.context_processors.site_address',
                'misago.core.context_processors.momentjs_locale',
                'misago.conf.context_processors.settings',
                'misago.search.context_processors.search_providers',
                'misago.users.context_processors.user_links',
                'misago.legal.context_processors.legal_links',

                # Data preloaders
                'misago.conf.context_processors.preload_settings_json',
                'misago.core.context_processors.current_link',
                'misago.markup.context_processors.preload_api_url',
                'misago.threads.context_processors.preload_threads_urls',
                'misago.users.context_processors.preload_user_json',

                # Note: keep frontend_context processor last for previous processors
                # to be able to expose data UI app via request.frontend_context
                'misago.core.context_processors.frontend_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Third party app settings

# Django Crispy Forms
#http://django-crispy-forms.readthedocs.io/en/latest/install.html

CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Django Debug Toolbar
# http://django-debug-toolbar.readthedocs.io/en/stable/configuration.html

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',

    'misago.acl.panels.MisagoACLPanel',

    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
]


# Django Rest Framework
# http://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'misago.core.rest_permissions.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'EXCEPTION_HANDLER': 'misago.core.exceptionhandler.handle_api_exception',
    'UNAUTHENTICATED_USER': 'misago.users.models.AnonymousUser',
    'URL_FORMAT_OVERRIDE': None,
}

CORS_ORIGIN_ALLOW_ALL = True # TODO: check if this needs to be changed for prod

JWT_AUTH = {
    'JWT_VERIFY_EXPIRATION': False # TODO: change this to expire in future
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


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        # Misago requires PostgreSQL to run
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'moshimoji',
        'USER': 'mmuser',
        'PASSWORD': '@we7Qsd6mm',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS': {
            'user_attributes': ['username', 'email'],
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 7,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/' # path @ which to serve static files


# The absolute path to the directory where collectstatic will collect static files for deployment.
# https://docs.djangoproject.com/en/1.11/ref/settings/#static-root

# NOTE: in misago STATIC_ROOT is {ROOT_DIR}/static:
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# TODO: determine if I need to worry about this discrepancy (e.g. with nginx settings) or if
# Django will take care of everything relative to my setting.
STATIC_ROOT = str(ROOT_DIR('staticfiles'))


# Dirs for Django to collect static files from
# This setting defines the additional locations the staticfiles app will traverse if the FileSystemFinder finder
# is enabled, e.g. if you use the collectstatic or findstatic management command or use the static file serving view.
# https://docs.djangoproject.com/en/1.10/ref/settings/#staticfiles-dirs

STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
    str(APPS_DIR.path('theme/static')),
)


# This setting defines the additional locations the staticfiles app will traverse if the FileSystemFinder finder
# is enabled, e.g. if you use the collectstatic or findstatic management command or use the static file serving view.
# https://docs.djangoproject.com/en/1.10/ref/settings/#staticfiles-dirs

STATICFILES_FINDERS = ( # specs for what files to look for
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# User uploads (Avatars, Attachments, files uploaded in other Django apps, ect.)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

MEDIA_URL = '/media/' # path @ which to serve media databases


# Absolute filesystem path to the directory that will hold user-uploaded files.
# i.e. collection dest for media files
# https://docs.djangoproject.com/en/1.11/ref/settings/#media-root

MEDIA_ROOT = str(APPS_DIR('media'))
