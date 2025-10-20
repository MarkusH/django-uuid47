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
INSTALLED_APPS = [
    "django_uuid47",
    "tests.testapp",
]
ROOT_URLCONF = "tests.urls"
TIME_ZONE = "UTC"

UUID47_KEY = "0123456789abcdef"
