from django.conf import settings
from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': settings('DB_NAME'),
        'USER': settings('DB_USER'),
        'PASSWORD': settings('DB_PASSWORD'),
        'HOST': settings('DB_HOST'),
        'PORT': settings('DB_PORT'),
    }
}


