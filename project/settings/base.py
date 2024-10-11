from unipath import Path
from decouple import config
import os

#
# BASE DIRECTORY
#
BASE_DIR = Path(__file__).ancestor(3)

#
# SECRET KEY
#
SECRET_KEY = config("SECRET_KEY")

#
# APPLICATIONS
#
DJANGO_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)

LOCAL_APPS = (
    "applications.participante",
    "applications.garaje",
    #
)

THIRD_PARTY_APPS = (
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

#
# REST FRAMEWORK
#
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}

#
# MIDDLEWARE
#
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

#
# ROOT URL CONFIGURATION
#
ROOT_URLCONF = "project.urls"

#
# TEMPLATES
#
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "garaje", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

#
# WSGI APPLICATION
#
WSGI_APPLICATION = "project.wsgi.application"

#
# PASSWORD VALIDATION
#
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

#
# INTERNATIONALIZATION
#
LANGUAGE_CODE = "en-us"

TIME_ZONE = config("TIME_ZONE")

USE_I18N = True

USE_L10N = True

USE_TZ = True

#
# DEFAULT PRIMARY KEY FIEDL TYPE
#
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#
# STATIC FILES
#
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # Ruta a la carpeta static
]
