import uuid

from dj_kaos_utils.models import HasAutoFields
from django.db import models
from django.utils.text import slugify


class HasUUIDModel(models.Model):
    """
    Add a unique UUID field to the model
    """

    class Meta:
        abstract = True

    uuid = models.UUIDField("UUID", unique=True, default=uuid.uuid4, editable=False)

    @property
    def shortcode(self):
        return str(self.uuid).split('-')[0]


class NamedModel(models.Model):
    """
    Model with a name field. `__str__` reflects the name.
    """

    class Meta:
        abstract = True

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name if self.name else super(NamedModel, self).__str__()


class SluggedModel(
    HasAutoFields,
    models.Model
):
    """
    Model with a slug field. Optionally autogenerate from another field denoted by `slug_source`
    """
    slug_source = None
    slug = models.SlugField(unique=True)

    def set_auto_fields(self):
        if self.slug_source and not self.slug:
            self.slug = slugify(getattr(self, self.slug_source))

    class Meta:
        abstract = True


__all__ = [
    'HasUUIDModel',
    'NamedModel',
    'SluggedModel',
]
