import os
import django_heroku
from pathlib import Path




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j^t&o#bd*mo9w6790i=e4w0k)d)q+601a3thtd(odht34&@)jq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app','healthbridgehospital-abd0b525c798.herokuapp.com','https://healthbridgehospital-abd0b525c798.herokuapp.com/','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 
    'home',

   
    'login',
    'crispy_forms',
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

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





# Custom Django auth settings
AUTH_USER_MODEL = 'login.User'
 




STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = "/login/login/"

LOGIN_URL = '/login/login/'

# LOGIN_EXEMPT_URLS = (
#     r'^login/logout/$',
#     r'^login/accounts/$',
#     r'^login/reset-password/$',
#     r'^login/reset-password/done/$',
#     r'login/reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>,+)/$',
#     r'^login/reset-password/complete/$',
# )


EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025




django_heroku.settings(locals())

from google.cloud import storage #herer is the error

import google.auth as auth
from google.oauth2 import service_account

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
   os.path.join('credential.json')
)

DEFAULT_FILE_STORAGE = 'website.gcloud.GoogleCloudMediaFileStorage'#'django.core.files.storage.FileSystemStorage'
GS_PROJECT_ID = 'realtors-356004'
GS_BUCKET_NAME = 'realtorsbucketheroku'
MEDIA_ROOT = 'media/'
UPLOAD_ROOT = 'media/uploads/'
MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_BUCKET_NAME)

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

