from __future__ import annotations

from django.db import models

from django_uuid47.fields import UUID47Field


class RegularFieldModel(models.Model):
    uuid = UUID47Field(blank=True)
    null_uuid = UUID47Field(null=True, blank=True)
