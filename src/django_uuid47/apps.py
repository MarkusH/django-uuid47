from __future__ import annotations

import python_uuidv47 as uuidv47
from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.signals import setting_changed


class DjangoUUID47AppConfig(AppConfig):
    name = "django_uuid47"

    def ready(self):
        set_keys()

        setting_changed.connect(set_key_receiver)


def set_keys() -> None:
    key = getattr(settings, "UUID47_KEY", None)
    if key is None:
        raise ImproperlyConfigured(
            "The UUID47_KEY setting is not configured. It must be a 16 bytes long string."
        )
    if isinstance(key, str):
        if len(key) != 16:
            raise ImproperlyConfigured(
                "The UUID47_KEY setting must be a 16 bytes long string."
            )
        key = key.encode()
    if not isinstance(key, bytes):
        raise ImproperlyConfigured(
            "The UUID47_KEY setting must be a 16 bytes long string."
        )

    key0, key1 = int.from_bytes(key[:8]), int.from_bytes(key[8:16])
    uuidv47.set_keys(key0, key1)


def set_key_receiver(setting, **kwargs) -> None:
    if setting == "UUID47_KEY":
        set_keys()
