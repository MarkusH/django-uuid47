=============
django-uuid47
=============

.. image:: https://img.shields.io/github/actions/workflow/status/MarkusH/django-uuid47/main.yml.svg?branch=main&style=for-the-badge
   :target: https://github.com/MarkusH/django-uuid47/actions?workflow=CI

.. image:: https://img.shields.io/badge/Coverage-100%25-success?style=for-the-badge
  :target: https://github.com/MarkusH/django-uuid47/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/django-uuid47.svg?style=for-the-badge
   :target: https://pypi.org/project/django-uuid47/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

Django support for `UUID47 <https://github.com/stateless-me/uuidv47>`__.

----

Requirements
------------

Python 3.14 supported.

Django 5.2 to 6.0 supported.

Installation
------------

Install with **pip**:

.. code-block:: sh

    python -m pip install django-uuid47

Then add to your installed apps:

.. code-block:: python

    INSTALLED_APPS = [
        ...,
        "django_uuid47",
        ...,
    ]

Next, define the setting ``UUID47_KEY`` as a 16 bytes long string for encryption of the UUIDs.

To generate a secret, use the ``token_bytes()`` function from the ``secrets`` stdlib module in a Python shell:

.. code-block:: python

    import secrets

    secrets.token_bytes(16)
    b"h\xd0\x0c\x9f\xfa\x99\xf75\x89J\x9c\xbe>l\x97\xf5"

Then, in the ``settings.py``:

.. code-block:: python

    UUID47_KEY = b"h\xd0\x0c\x9f\xfa\x99\xf75\x89J\x9c\xbe>l\x97\xf5"

Usage
-----

In models, use the ``django_uuid47.fields.UUID47Field()`` model field, like a regular model field.

In forms, use the ``django_uuid47.forms.UUID47Field()`` form field, like a regular form field.
