# In production set the environment variable like this:
#    DJANGO_SETTINGS_MODULE=wedding.settings.production
from .base import *             # NOQA
import logging.config

print("\x1b[7mRUNNING IN PRODUCTION MODE\x1b[0m")

# For security and performance reasons, DEBUG is turned off
DEBUG = False
TEMPLATE_DEBUG = False

# Must mention ALLOWED_HOSTS in production!
# ALLOWED_HOSTS = ["wedding.com"]

# Cache the templates in memory for speed-up
loaders = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

TEMPLATES[0]['OPTIONS'].update({"loaders": loaders})
TEMPLATES[0].update({"APP_DIRS": False})

# Define STATIC_ROOT for the collectstatic command
STATIC_ROOT = join(BASE_DIR, '..', 'site', 'static')

# Static files in s3
import environ
env = environ.Env()

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET_NAME')
AWS_S3_CALLING_FORMAT = 'boto.s3.connection.OrdinaryCallingFormat'

STATIC_URL = 'https://mikeandzoey.com.s3.amazonaws.com/static/'

# see http://developer.yahoo.com/performance/rules.html#expires
AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
    'Cache-Control': 'max-age=86400',
}

# Log everything to the logs directory at the top
LOGFILE_ROOT = join(dirname(BASE_DIR), 'logs')

# Reset logging
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(pathname)s:"
                      "%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'proj_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': join(LOGFILE_ROOT, 'project.log'),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'project': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(LOGGING)
