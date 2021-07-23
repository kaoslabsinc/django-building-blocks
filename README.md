# Django Building Blocks

Abstract Django base models (and model class factories) to act as building blocks for rapid development of Django
database models

## Quick start

```shell
pip install django-building-blocks
```

## Classes provided

Check the docstring under each class for their documentation.

### Mixin model classes

- [`HasInitials`](building_blocks/models/mixins.py#L4)

### Abstract model classes

- [`HasUUID`](building_blocks/models/abstracts.py#L10)
- [`Archivable`](building_blocks/models/abstracts.py#L25)
- [`Publishable`](building_blocks/models/abstracts.py#L48)

### Admin Block classes

Admin blocks aren't meant to be inherited by your model's admin class. Instead, each field in the admin block is used to
create your desired admin class. For example:

```python
# example/sample/admin.py

@admin.register(ArchivableHasUUID)
class ArchivableHasUUIDAdmin(
    ArchivableAdmin,  # Inheritable admin to add common functionality. More on this later. 
    admin.ModelAdmin
):
    search_fields = (
        *HasUUIDAdminBlock.search_fields,  # AdminBlock to assist in shaping the admin
    )
    list_display = (
        *HasUUIDAdminBlock.list_display,
        *ArchivableAdminBlock.list_display,
    )
    list_filter = (
        *ArchivableAdminBlock.list_filter,
    )

    readonly_fields = (
        *HasUUIDAdminBlock.readonly_fields,
        *ArchivableAdminBlock.readonly_fields,
    )
    fieldsets = (
        *HasUUIDAdminBlock.fieldsets,
        *ArchivableAdminBlock.fieldsets,
    )
```

As its name suggests, the model `ArchivableHasUUID` inherits from both `Archivable` and `HasUUID` and thus has fields
form both. With admin blocks you can create `ArchivableHasUUIDAdmin` without mentioning individual fields from each
class, adding to the conciseness of your code. It'll also make it hard to miss a field since the AdminBlock has the
default and recommended fields for each admin setting.

Available Admin Blocks:

- [`HasUUIDAdminBlock`](building_blocks/admin/blocks.py#L10)
- [`ArchivableAdminBlock`](building_blocks/admin/blocks.py#L25)
- [`PublishableAdminBlock`](building_blocks/admin/blocks.py#L35)
- [`HasInitialsAdminBlock`](building_blocks/admin/blocks.py#L45)

### Inheritable Admin classes

Unlike Admin Blocks the following classes are meant to be inherited by your admin class. The usually provide
functionality such as common admin actions to your admin.

- [`ArchivableAdmin`](building_blocks/admin/admin.py#L9)
- [`PublishableAdmin`](building_blocks/admin/admin.py#L37)

Please note that the majority of the above classes
use [django-object-actions](https://github.com/crccheck/django-object-actions) to enable admin actions on objects'
`admin:change` pages. To enable this functionality add `'django_object_actions'` to your `INSTALLED_APPS`.

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
