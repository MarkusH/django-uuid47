from __future__ import annotations

import uuid

import python_uuidv47 as uuidv47
from django.test import TestCase

from django_uuid47 import forms
from django_uuid47.fields import UUID47Field
from tests.testapp.forms import RegularFieldForm

from .testapp.models import RegularFieldModel


class UUID47FieldTests(TestCase):
    def test_regular_field(self):
        obj = RegularFieldModel()

        assert isinstance(obj.uuid, uuid.UUID)
        assert obj.uuid.version == 7

        # Because of "default=uuid7" it's not None
        assert isinstance(obj.null_uuid, uuid.UUID)
        assert obj.null_uuid.version == 7

    def test_regular_field_saved(self):
        RegularFieldModel.objects.create(null_uuid=None)

        obj = RegularFieldModel.objects.get()

        assert isinstance(obj.uuid, uuid.UUID)
        assert obj.uuid.version == 7
        assert obj.null_uuid is None

    def test_deconstruct(self):
        f = RegularFieldModel._meta.get_field("uuid")

        name, path, _, _ = f.deconstruct()

        assert name == "uuid"
        assert path == "django_uuid47.fields.UUID47Field"

    def test_deconstruct_overridden_default(self):
        f = UUID47Field(default=uuid.uuid4)

        _, _, _, kwargs = f.deconstruct()

        assert "default" not in kwargs

    def test_formfield(self):
        f = UUID47Field()

        formfield = f.formfield()

        assert isinstance(formfield, forms.UUID47Field)


class UUID47FormFieldTests(TestCase):
    def test_save(self):
        form = RegularFieldForm(data={})

        assert form.is_valid()
        assert form.cleaned_data == {"uuid": None, "null_uuid": None}

        obj = form.save()

        assert isinstance(obj.uuid, uuid.UUID)
        assert obj.uuid.version == 7
        # Because of "default=uuid7" it's not None
        assert isinstance(obj.null_uuid, uuid.UUID)
        assert obj.null_uuid.version == 7

    def test_versions(self):
        obj = RegularFieldModel()
        form = RegularFieldForm(instance=obj)

        assert form.initial["uuid"].version == 7
        assert form.initial["null_uuid"].version == 7

        uuid_v4 = uuidv47.encode(str(form.initial["uuid"]))
        null_uuid_v4 = uuidv47.encode(str(form.initial["null_uuid"]))

        assert uuid_v4 in str(form)
        assert null_uuid_v4 in str(form)

    def test_vectors(self):
        v4 = uuid.UUID("2ff64574-c29e-41d4-a716-446655440000")
        v7 = uuid.UUID("550e8400-e29b-71d4-a716-446655440000")
        with self.settings(
            UUID47_KEY=b"\x12\x34\x56\x78\x9a\xbc\xde\xf0\xfe\xdc\xba\x98\x76\x54\x32\x10"
        ):
            form = RegularFieldForm(data={"uuid": v4})
            assert form.is_valid()
            assert form.cleaned_data["uuid"] == v7
            obj = form.save()
            obj.refresh_from_db()
            assert obj.uuid == v7
