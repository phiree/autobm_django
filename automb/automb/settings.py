"""
Django settings for automb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xbq2ow6t&2tdmd-xd=)j2@%9loe6stext2p$*vhltghyce#ong'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'unique_random',
    #'django.contrib.gis',
    'car_service',
    'userprofile',

)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'car_service.middleware.MobileMiddleware',
)
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'permission.backends.PermissionBackend',
)
TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
'django.core.context_processors.request',  # added for django-formsbuilder
)
ROOT_URLCONF = 'automb.urls'
AUTH_PROFILE_MODULE = 'userprofile.UserProfile'
WSGI_APPLICATION = 'automb.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE':'mysql.connector.django',
        'NAME': '92auto',
        'USER': '92auto',
        'PASSWORD': 'twgdhbtzhy',
        'HOST': '127.0.0.1',
        'ATOMIC_REQUESTS':True,
    'sqlite':
            {
               'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, '92auto.sqlite3'),
            }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL  = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL='/media/'

LOGIN_REDIRECT_URL='/'
WSGI_LOG=os.path.join(BASE_DIR,'wsgi_log.log')
# 模板文件夹名称不能是 templates , 否则会被 template_loader 优先取用,致使这里的设置失效
TEMPLATE_DIRS_MOBILE=(join(BASE_DIR,'car_service/templates_mobile'),)
TEMPLATE_DIRS_DESKTOP=(join(BASE_DIR,'car_service/templates_desktop'),)
SOUTH_TESTS_MIGRATE = False
