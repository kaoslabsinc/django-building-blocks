import uuid

from django.db import models


class HasUUID(models.Model):
    class Meta:
        abstract = True

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    @property
    def uuid_str(self):
        return str(self.uuid)

    @property
    def shortcode(self):
        return self.uuid_str.split('-')[0]
