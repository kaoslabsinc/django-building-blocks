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

By using this library you can create models in such a way to make their fields standard across your entire project and
all your projects. For example:

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

Note that we did not need to add anything to the body of the above model. This model is entirely composed of abstract
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
in this library, have an associated Admin Block class, that enables you to define admin for their inheritors in a
standard way. For example in the case of `Publishable`, you would probably like to show the publication status and date
in `list_display`. Instead of having to remember to include both fields in all your admins, you can just include the
Admin Block in the way showed above and have the fields show up in the list table for all the inheritors
of `Publishable`.

## Details and classes provided

Note: Check the docstring under each class for their documentation.

### Abstract models

[Django Model Behaviors](https://blog.kevinastone.com/django-model-behaviors) describes a design pattern for developing
django models that makes them compositional. For example, your project might have the ability to post blog
posts (`BlogPost`), and each post goes through 3 stages: Draft, Published, and Archived. In your project, your users
might also have the ability to post shorter status updates (`StatusUpdate`), and you'd like those status updates to also
go through a similar publishing pipeline. Furthermore, both `BlogPost` and `StatusUpdate` are timestamped with the date
and time they are published.

As a seasoned developer, instead of coding the functionality on both models, you would create an abstract model, let's
call it `Publishable`, and have both `BlogPost` and `StatusUpdate` inherit from it. Now you have abstracted away common
functionality between your models, into the `Publishable` interface/abstract model. Not only this is DRY, but also if
you like to make updates to how your publishing pipeline works, you can just update `Publishable` and both `BlogPost`
and `StatusUpdate` would get updated with the new pipeline.

`django-building-blocks` provides a number of such abstract models:

- [`HasUUID`](building_blocks/models/abstracts.py)
- [`Archivable`](building_blocks/models/abstracts.py)
- [`Publishable`](building_blocks/models/abstracts.py)

### Abstract model factories

Abstract model factories enable you to create abstract models on the fly. Abstract model factories enable you to modify
the inherited fields dynamically from the same base class. For example, you might have a model that will have an `email`
field. You can use `HasEmailFactory.as_abstract_model()` that returns an abstract model that can be inherited from. Now
say you have another model that also has a email, but the email here is an optional field (`blank=True`). Instead of
creating a whole new abstract model (like `HasOptionalEmail`), you can inherit
from `HasEmailFactory.as_abstract_model(optional=True)` which will return an abstract model with the same `email` field,
but this time the `email` field is optional.

Abstract model factories provided:

- [`HasNameFactory`](building_blocks/models/factories.py)
- [`HasEmailFactory`](building_blocks/models/factories.py)
- [`HasDescriptionFactory`](building_blocks/models/factories.py)
- [`HasCoverPhotoFactory`](building_blocks/models/factories.py)
- [`HasIconFactory`](building_blocks/models/factories.py)
- [`HasUserFactory`](building_blocks/models/factories.py)
- [`HasAutoCodeFactory`](building_blocks/models/factories.py)
- [`HasAutoSlugFactory`](building_blocks/models/factories.py)

You can create your own abstract model factory by inheriting
from `building_blocks.models.factories.AbstractModelFactory`. Check some of the implementations for an example.

### Mixin model classes

- [`HasInitials`](building_blocks/models/mixins.py)
- [`HasAutoFields`](building_blocks/models/mixins.py)

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
default and recommended fields for each admin field.

Available Admin Blocks:

- [`HasUUIDAdminBlock`](building_blocks/admin/blocks.py)
- [`ArchivableAdminBlock`](building_blocks/admin/blocks.py)
- [`PublishableAdminBlock`](building_blocks/admin/blocks.py)
- [`HasInitialsAdminBlock`](building_blocks/admin/blocks.py)
- [`HasNameAdminBlock`](building_blocks/admin/blocks.py)
- [`HasEmailAdminBlock`](building_blocks/admin/blocks.py)
- [`HasDescriptionAdminBlock`](building_blocks/admin/blocks.py)
- [`HasCoverPhotoAdminBlock`](building_blocks/admin/blocks.py)
- [`HasIconAdminBlock`](building_blocks/admin/blocks.py)
- [`HasUserAdminBlock`](building_blocks/admin/blocks.py)
- [`HasAutoSlugAdminBlock`](building_blocks/admin/blocks.py)
- [`TimeStampedModelAdminBlock`](building_blocks/admin/blocks.py)

### Inheritable Admin classes

Unlike Admin Blocks the following classes are meant to be inherited by your admin class. The usually provide
functionality such as common admin actions to your admin.

- [`ArchivableAdmin`](building_blocks/admin/admin.py)
- [`PublishableAdmin`](building_blocks/admin/admin.py)
- [`HasUserAdmin`](building_blocks/admin/admin.py)

Please note that the majority of the inheritable admins
use [django-object-actions](https://github.com/crccheck/django-object-actions) to enable admin actions on objects'
`admin:change` pages. To enable this functionality add `'django_object_actions'` to your `INSTALLED_APPS` so your
project can find the templates from `django_object_actions` which are used in rendering the buttons for the actions.

### Mixin Admin classes

- [`CheckUserAdminMixin`](building_blocks/admin/mixins.py)
- [`EditReadonlyAdminMixin`](building_blocks/admin/mixins.py)
- [`HasAutoSlugAdminMixin`](building_blocks/admin/mixins.py)
- [`DjangoObjectActionsPermissionsMixin`](building_blocks/admin/mixins.py)

### Admin inline mixins

When you need some fields on an inline admin to be readonly only for editing (equivalent of `EditReadonlyAdminMixin`),
you have to split the interface into two inlines, one for adding which doesn't show any objects, and one for listing
them, which has the readonly fields defined. The following classes facilitate this design pattern:

- [`AddInlineMixin`](building_blocks/admin/inlines.py)
- [`ListInlineMixin`](building_blocks/admin/inlines.py)
- [`ReadOnlyInlineMixin`](building_blocks/admin/inlines.py)

## HTML render utilities

They are used in conjunction with `@admin.display` to render html such as anchor tags, or images on the admin.

- [`json_field_pp`](building_blocks/admin/utils.py)
- [`render_element`](building_blocks/admin/utils.py)
- [`render_img`](building_blocks/admin/utils.py)
- [`render_anchor`](building_blocks/admin/utils.py)

## Forms

### `UnrequiredFieldsForm` and `unrequire_form`

Make fields that are usually required in a model form, be not required. Used in conjunction with `HasAutoFields`, since
the fields that aren't required are auto set. Also used in conjunction with `EditReadonlyAdminMixin` to allow manual
setting of a field upon creation.

## Fields

- [`CaseInsensitiveFieldMixin`](building_blocks/fields.py)
- [`ToLowerCaseFieldMixin`](building_blocks/fields.py)
- [`LowerCaseCharField`](building_blocks/fields.py)

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
