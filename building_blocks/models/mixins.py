from django.db import models


class HasUUIDModel(models.Model):
    """
    Add a unique UUID field to the model
    """

    class Meta:
        abstract = True

    uuid = models.UUIDField("UUID", unique=True, default=uuid.uuid4, editable=False)

    @property
    def shortcode(self):
        return self.uuid_str.split('-')[0]


class NamedModel(models.Model):
    """
    Model with a name field. __str__ reflects the name.
    """

    class Meta:
        abstract = True

    name = models.CharField(max_length=255, **kwargs)

    def __str__(self):
        return self.name if self.name else super(NamedModel, self).__str__()


__all__ = [
    'HasUUIDModel',
    'NamedModel',
]
