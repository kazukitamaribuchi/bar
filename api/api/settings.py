from pathlib import Path
import os
import logging
import environ
import datetime

env = environ.Env()
env.read_env('.env')


logging.basicConfig(
    level = logging.DEBUG,
    format = '''%(levelname)s %(asctime)s %(pathname)s:%(funcName)s 行数:%(lineno)s:%(lineno)s
    %(message)s''')

logger = logging.getLogger(__name__)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

if os.environ['DJANGO_ENV'] == 'production':
    # 本番
    DEBUG = False
else:
    # 開発
    DEBUG = True

ALLOWED_HOSTS = ['*']

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_jwt',\
    'django_filters',
    'crm.apps.CrmConfig',
    # 'corsheaders',
    # 'webpack_loader',
    'ws.apps.WsConfig',
    'channels',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '100/day',
    #     'user': '20/sec',
    # }
}


JWT_AUTH = {
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=86400), # Sessionの保存期間を設定(24時間)
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7), # Sessionの保存期間を設定(1週間)
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    # 'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(seconds=1),
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
        # 'CONFIG': {
        #     'hosts':[os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        # },
    },
}


if not DEBUG:
    CHANNEL_LAYERS['default'].update({
        'CONFIG': {
            'hosts':[os.environ.get('REDIS_URL', ('redis', 6379))],
        },
    })

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'api.wsgi.application'
ASGI_APPLICATION = 'api.routing.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


AUTH_USER_MODEL = 'crm.mUser'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CORS_ORIGIN_ALLOW_ALL = True
#
# from corsheaders.defaults import default_headers
#
# CORS_ALLOW_HEADERS = default_headers + (
#     'access-control-allow-origin',
# )
#
# CORS_ALLOW_CREDENTIALS = True
#
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:8080',
# )

if DEBUG:
    logging.basicConfig(
        level = logging.DEBUG,
        format = '''%(levelname)s %(asctime)s %(pathname)s:%(funcName)s:%(lineno)s
        %(message)s''')
    INSTALLED_APPS += ['corsheaders']
    MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE
    from corsheaders.defaults import default_headers
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:8080',
    )
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_HEADERS = default_headers + (
        'access-control-allow-origin',
    )

else:
    import dj_database_url
    DATABASE_URL = os.environ.get('DATABASE_URL')
    db_from_env = dj_database_url.config(default=DATABASE_URL, ssl_require=True)
    DATABASES['default'].update(db_from_env)
    logging.basicConfig(
        level = logging.DEBUG,
        format = '''%(levelname)s %(asctime)s %(pathname)s:%(funcName)s 行数:%(lineno)s:%(lineno)s
        %(message)s'''
        # filename = 'logs/debug.log',
        # filemode = 'a'
    )
    INSTALLED_APPS += [
        'cloudinary',
        'cloudinary_storage',
    ]
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': os.environ['CLOUD_NAME'],
        'API_KEY':  os.environ['CLOUDINARY_API_KEY'],
        'API_SECRET': os.environ['CLOUDINARY_API_SECRET']
    }
