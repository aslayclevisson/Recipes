# flake8: noqa
from .base import *

DEBUG = True

INTERNAL_IPS = ['localhost', '127.0.0.1']

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
