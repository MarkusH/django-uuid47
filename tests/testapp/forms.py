from __future__ import annotations

from django import forms

from .models import RegularFieldModel


class RegularFieldForm(forms.ModelForm):
    class Meta:
        model = RegularFieldModel
        fields = "__all__"
