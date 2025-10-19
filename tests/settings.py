from __future__ import annotations

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "NOTASECRET"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}

ALLOWED_HOSTS: list[str] = []

INSTALLED_APPS = [
    "django_uuid47",
]

MIDDLEWARE: list[str] = []

ROOT_URLCONF = "tests.urls"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True

USE_TZ = True
