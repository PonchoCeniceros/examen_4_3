import os
from .base import *
from decouple import config

#
# DEBUG FLAG
#
DEBUG = True

#
# ALLOWED HOSTS
#
ALLOWED_HOSTS=['*']
CORS_ORIGIN_ALLOW_ALL = True

#
# DATABASE
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
    }
}

#
# STATIC FILES
#
STATIC_URL = '/admin/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'admin/static')
