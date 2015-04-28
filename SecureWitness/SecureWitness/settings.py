
"""
Django settings for SecureWitness project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


'''
Things to Change Back:
Heroku Deployment Chango
Comment out DEBUG=True
Change back DATABASES
UnComment out DEBUD=False
'''
# heroku deployment change
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5uv!jzjc_3#h077wtz(a8j(+(4-@jw!!((auxlf)(=$7b_o9ga'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ENV_PATH, 'media/') 
MEDIA_URL = 'media/'
LOGIN_URL = '/Login/'
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Login',
    'SecureWitness',
    'gunicorn'
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SecureWitness.urls'


WSGI_APPLICATION = 'SecureWitness.wsgi.application'




# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# heroku changes, we now have switched to postgresql I believe



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

#commented out from django project default for heroku deployment
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
#for heroku deployment as well
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

import dj_database_url
DATABASES = { 'default' : dj_database_url.config()}

STATIC_ROOT = 'staticfiles'

DEBUG = True

try:
    from SecureWitness.local_settings import *
except ImportError:
    pass
