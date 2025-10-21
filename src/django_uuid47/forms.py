from __future__ import annotations

import uuid

import python_uuidv47 as uuidv47
from django import forms
from django.core.exceptions import ValidationError


class UUID47Field(forms.CharField):
    default_error_messages = forms.UUIDField.default_error_messages

    def prepare_value(self, value):
        if isinstance(value, uuid.UUID):
            value = str(value)
        return uuidv47.encode(value)

    def to_python(self, value):
        value_v4 = super().to_python(value)
        if value_v4 in self.empty_values:
            return None
        try:
            value_v7 = uuidv47.decode(value_v4)
        except ValueError:
            raise ValidationError(self.error_messages["invalid"], code="invalid")
        return uuid.UUID(value_v7)
