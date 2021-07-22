# Django Building Blocks

Abstract Django base models (and model class factories) to act as building blocks for rapid development of Django
database models

## Quick start

```shell
pip install django-building-blocks
```

## Abstract model classes

- `HasUUID`
- `Archivable`
- `Publishable`

## Mixin model classes

- `HasInitials`

## Admin Block classes

Admin blocks aren't meant to be inherited by your model's admin class. Instead, each field in the admin block is used to
create your desired admin class. For an example check out `example/sample/admin.py:HasUUIDExampleAdmin`

Available Admin Blocks:

- `HasUUIDAdminBlock`
- `ArchivableAdminBlock`
- `PublishableAdminBlock`
- `HasInitialsAdminBlock`

## Development and Testing

### IDE Setup

Add the `example` directory to the `PYTHONPATH` in your IDE to avoid seeing import warnings in the `tests` modules. If
you are using PyCharm, this is already set up.

### Running the Tests

Install requirements

```
pip install -r requirements.txt
```

For local environment

```
pytest
```

For all supported environments

```
tox
```
