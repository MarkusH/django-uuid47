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

Python 3.9 to 3.14 supported.

Django 4.2 to 6.0 supported.

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

Usage
-----

