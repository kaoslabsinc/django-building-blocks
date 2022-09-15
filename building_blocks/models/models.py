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


__all__ = [
    'HasUUIDModel',
]
