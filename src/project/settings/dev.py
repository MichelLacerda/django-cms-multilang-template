from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

ENABLE_DJANGO_DEBUG_TOOLBAR = True

if ENABLE_DJANGO_DEBUG_TOOLBAR:

    INSTALLED_APPS = INSTALLED_APPS + [
        "debug_toolbar",
    ]

    MIDDLEWARE = MIDDLEWARE + [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

    INTERNAL_IPS = ["127.0.0.1", "localhost"]
