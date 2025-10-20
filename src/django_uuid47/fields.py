from __future__ import annotations

import uuid

from django.db import models

from . import forms


class UUID47Field(models.UUIDField):
    def __init__(self, verbose_name=None, **kwargs):
        kwargs["default"] = uuid.uuid7
        super().__init__(verbose_name, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["default"]
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "form_class": forms.UUID47Field,
                **kwargs,
            }
        )
