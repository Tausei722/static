"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# env.read os.getenv(os.path.join(BASE_DIR, '.env'))
dotenv_path=os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dotenv_path)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
# SECRET_KEY = 'django-insecure-q%-s8gf-6reuvl(j*fp+n0^whrp0i4_t@aewm6wf8bq2warg=0'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'flash',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# MIDDLEWARE_CLASSES = [
#     'WhiteNoiseMiddleware',
# ]
ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
    'ENGINE':'django.db.backends.postgresql',
    # 'NAME': os.getenv('DB_NAME'),
    # 'USER': os.getenv('DB_USER'),
    # 'PASSWORD': os.getenv('DB_PASSWORD'),
    # 'HOST': os.getenv('DB_HOST'),
    # 'PORT': os.getenv('DB_PORT'),
    'NAME': 'delv2baclv0ejf',
    'USER': 'u45n86j6die9je',
    'PASSWORD': 'pf164df82c00df1b3736dcf71670dbabb00dd3c3d2dd380d433b4ccd8fa5f3414',
    'HOST': 'ec2-23-23-160-238.compute-1.amazonaws.com',
    'PORT': 5432,
}
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

# settings.py
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    os.getenv("HASHER"),
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = '/mysite/static'
STATICFILES_DIRS = []
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

AUTH_USER_MODEL = 'flash.CustomUser'

# settings.py
# CSRF_FAILURE_VIEW = 'flash.views.your_custom_view'
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    'https://rio-app-d82eb8d186ab.herokuapp.com/',
    'https://rio-app-d82eb8d186ab.herokuapp.com/flash',
    'https://rio-app-d82eb8d186ab.herokuapp.com/flash/signin',
    'https://rio-app-d82eb8d186ab.herokuapp.com/flash/login',
]
CORS_ORIGIN_WHITELIST = [
    'https://rio-app-d82eb8d186ab.herokuapp.com/',
]
ALLOWED_HOSTS = ['rio-app-d82eb8d186ab.herokuapp.com']