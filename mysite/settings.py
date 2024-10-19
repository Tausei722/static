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
import dj_database_url
import cloudinary
import cloudinary_storage

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
DEBUG = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'corsheaders',
    'flash',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
MIDDLEWARE_CLASSES = [
    'WhiteNoiseMiddleware',
]
ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/'),
            os.path.join(BASE_DIR, 'templates/flash/.herokuapp.com'),
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
    'NAME': os.getenv('DB_NAME'),
    'USER': os.getenv('DB_USER'),
    'PASSWORD': os.getenv('DB_PASSWORD'),
    'HOST': os.getenv('DB_HOST'),
    'PORT': os.getenv('DB_PORT'),
    # 'NAME': 'delv2baclv0ejf',
    # 'USER': 'u45n86j6die9je',
    # 'PASSWORD': 'pf164df82c00df1b3736dcf71670dbabb00dd3c3d2dd380d433b4ccd8fa5f3414',
    # 'HOST': 'ec2-23-23-160-238.compute-1.amazonaws.com',
    # 'PORT': 5432,
}
}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
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

#動画保存のためのツール設定
CLOUDINARY_STORAGE  = {
    'CLOUD_NAME':os.getenv('CLOUDINARY_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
    # 'CLOUD_NAME': 'dumlzpddn',
    # 'API_KEY': 231167484435616,
    # 'API_SECRET': '-eZ0nip0L202BnTt0JfF3UQLS1k',
}
# settings.py
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(STATIC_ROOT, 'css'),
    os.path.join(STATIC_ROOT, 'js'),
    os.path.join(STATIC_ROOT, 'images'),
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'flash.CustomUser'

# settings.py
# CSRF_FAILURE_VIEW = 'flash.views.csrf_custom_view'
CSRF_TRUSTED_ORIGINS = ['https://rio-app-d82eb8d186ab.herokuapp.com']
# CSRF_ALLOWED_ORIGINS = ['https://rio-app-d82eb8d186ab.herokuapp.com']
# CORS_ORIGIN_WHITELIST = ['https://*.rio-app-d82eb8d186ab.herokuapp.com']
# CORS_ALLOWED_ORIGIN_REGEX = r'^https://rio-app-d82eb8d186ab\.herokuapp\.com$'
# CSRF_COOKIE_DOMAIN = '.herokuapp.com'
ALLOWED_HOSTS = ['rio-app-d82eb8d186ab.herokuapp.com']
CORS_ORIGIN_ALLOW_ALL = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True