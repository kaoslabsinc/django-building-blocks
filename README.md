# Django Building Blocks

Abstract Django base models (and model class factories) to act as building blocks for rapid development of Django
database models

## Quick start

```shell
pip install django-building-blocks
```

## Rationale

`django-building-blocks` provides common design patterns and behaviours that repeat themselves during the development of
django projects. The main aim of this package is to provide common interfaces for the development of django models. This
portion of this library is inspired by Kevin Stone's excellent blog
post [Django Model Behaviors](https://blog.kevinastone.com/django-model-behaviors). The secondary aim of this library is
to provide interfaces and mixins for Django admin classes, so you can add functionality to your admin pages really fast,
without the need to Google solutions and look at Stackoverflow for answers.

By using library you can create models in such a way to make their fields standard across your entire project and all
your projects. For example:

```python
class BlogPost(
    HasNameFactory.as_abstract_model(),
    HasDescription,
    HasHTMLBody,
    Publishable,
    models.Model
):
    pass
```

Note that we did not need to add anything to the body of the above model. The model is entirely composed of abstract
models (and abstract model factories - more on this later). If you have another model:

```python
class WebPage(
    HasNameFactory.as_abstract_model(),
    HasAutoSlugFactory.as_abstract_model(),
    HasHTMLBody,
    Publishable,
    models.Model
):
    pass
```

Note the similarity between the two models. Now instead of having to code the fields, associated properties and
behaviors on each model individually, you can reuse them infinite times, and keep them standard across your project (and
all your projects).

The admin class for `BlogPost` would look something like this:

```python
@admin.register(BlogPost)
class BlogPostAdmin(
    PublishableAdmin,
    admin.ModelAdmin
):
    list_display = (
        *HasNameAdminBlock.list_display,
        *PublishableAdminBlock.list_display,
        ...
    )
    ...
```

Notice how we have composed each element in the admin using a concept called Admin Blocks. Each of the abstract classes
in this library, have an associated Admin Block class, that enables you to define admin for their inheritos in an
standard way. For example in the case of `Publishable`, you would probably like to show the publication status and date
in the `list_display`. Instead of having to remember to include both fields in all your admins, you can just include the
Admin Block in the way showed and have the fields show up in the list table for all the inheritors of `Publishable`.

## Abstract models and Abstract model factories

### Abstract models

Kevin Stone's blog post [Django Model Behaviors](https://blog.kevinastone.com/django-model-behaviors) describes a design
pattern for developing django models that makes them compositional. For example, your project might have the ability to
post blog posts (`BlogPost`), and each post goes through 3 stages: Draft, Published, and Archived. In your project, your
users might also have the ability to post shorter status updates (`StatusUpdate`), and you'd like those status updates
to also go through a similar publishing pipeline. Furthermore, both `BlogPost` and `StatusUpdate` are timestamped with
the date and time they are published.

As a seasoned developer, instead of coding the functionality on both models, you would create an abstract model, let's
call it `Publishable`, and have both `BlogPost` and `StatusUpdate` inherit from it. Now you have abstracted away common
functionality between your models, into the `Publishable` interface/abstract model. Not only this is DRY, but also if
you like to make updates to how your publishing pipeline works, you can just update `Publishable` and both `BlogPost`
and `StatusUpdate` would get updated with the new pipeline.

`django-building-blocks` provides a number of such abstract models:

- [`HasUUID`](building_blocks/models/abstracts.py#L10)
- [`Archivable`](building_blocks/models/abstracts.py#L25)
- [`Publishable`](building_blocks/models/abstracts.py#L48)

## Classes provided

Check the docstring under each class for their documentation.

### Mixin model classes

- [`HasInitials`](building_blocks/models/mixins.py#L4)

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
