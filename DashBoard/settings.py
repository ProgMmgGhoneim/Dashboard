"""
Django settings for DashBoard project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&im+y1q-$2+m^j)kk8+1zc7d27&zl=_9nfc-s1-^pu%20d=(vl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'oauth2_provider',
    'import_export',
    'rangefilter',
    'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DashBoard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'DashBoard/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DashBoard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'DashBoard/static'),
)

IMPORT_EXPORT_IMPORT_PERMISSION_CODE = 'view' # related to permission
IMPORT_EXPORT_USE_TRANSACTIONS = True

# OAuth application setting
# LOGIN_URL='/admin/login/'
# AUTH_USER_MODEL='users.User'

# NAME=dashboard_app
# ID="LzMySwilXEs7q8Ynpwm2HOYrjbBCmzB1mOfHRPW7"
# SECRET="jzdbVfYP3tesS1Mjoh7wO6t1Pa3yGtuvvzaRrNsjXFZa0RdCZlrNCD3Ngm83P4iJSvrRzOtV0O0RlTvsSz4YDJqYllL0HZmntYRbKrCpLexTTnMkcTibNyBumMrNTW0J"
# Client type: confidential
# Authorization Grant Type: `authorization-code`
# Redirect Uris: http://127.0.0.1:8000/admin
# CODE="82Gv1JyvoN29bV6NoecSydTuiCxCIu"

# OAuth client settings
# NAME=client_creadintial
# ID="YCMrrGuC7KvjHFJpKHYAhzkFy7o59xisxxlbjuUj"
# SECRET=cDgGcLH0vTAjK1o1Spo2EHHePCJweD5dYCbTxCLaEZRjuzKrPw6hu8MjsiXIo6brTQ38FWKejmniLegAOenQFjfSulVVfq37d8fouYHegnrScSGh6A1ev4K6m1nF59XY
# Client type: confidential
# Authorization Grant Type: `client-credentials`
# Redirect Uris: http://127.0.0.1:8000/admin
# CREADINTIAL: WUNNcnJHdUM3S3ZqSEZKcEtIWUFoemtGeTdvNTl4aXN4eGxianVVajpjRGdHY0xIMHZUQWpLMW8xU3BvMkVISGVQQ0p3ZUQ1ZFlDYlR4Q0xhRVpSanV6S3JQdzZodThNanNpWElvNmJyVFEzOEZXS2VqbW5pTGVnQU9lblFGamZTdWxWVmZxMzdkOGZvdVlIZWduclNjU0doNkExZXY0SzZtMW5GNTlYWQ==

