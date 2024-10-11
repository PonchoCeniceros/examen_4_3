import os
from .base import *

#
# DEBUG FLAG
#
DEBUG = True

#
# ALLOWED HOSTS
#
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True

#
# DATABASE
#
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR.child("db.sqlite3"),
    }
}
