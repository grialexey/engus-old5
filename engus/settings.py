
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(__file__)


INSTALLED_APPS = (
    # Django contrib apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third-party apps, patches, fixes
    'easy_thumbnails',
    #'rest_framework',
    #'debug_toolbar',
    'pytils',
    'ckeditor',
    'django_select2',

    # Application base, containing global templates.
    'engus.accounts',
    'engus.cards',
    'engus.articles',

    # Local apps, referenced via engus.appname


    'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    'engus.cards.context_processors.cards_to_repeat_count',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

ROOT_URLCONF = 'engus.urls'

WSGI_APPLICATION = 'engus.wsgi.application'


# Internationalization

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Media and Static Files

MEDIA_ROOT = '/var/webapps/engus/www/media/'

MEDIA_URL = '/media/'

STATIC_ROOT = '/var/webapps/engus/www/static/'

STATIC_URL = '/static/'


#APPEND_SLASH = False

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

LOGIN_REDIRECT_URL = '/'

SITE_ID = 1


# Third-party apps settings

# easy-thumbnails
THUMBNAIL_SUBDIR = 'thumbs'

# rest framework
# REST_FRAMEWORK = {
#     'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
# }

CKEDITOR_UPLOAD_PATH = 'ckeditor_uploads/'

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Undo', 'Redo'],
            ['Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', ],
            # ['FontSize'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', ],
            # ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'],
        ],
        'height': 500,
        'width': 635,
    },
}

from .local_settings import *
