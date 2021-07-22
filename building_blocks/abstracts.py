import uuid

from django.db import models
from django.utils.timezone import now

from .querysets import ArchivableQueryset


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


class Archivable(models.Model):
    class Meta:
        abstract = True

    archived_at = models.DateTimeField(null=True, blank=True)

    @property
    def is_active(self):
        return self.archived_at is None

    @property
    def archive_status(self):
        return 'archived' if self.archived_at else 'active'

    def archive(self):
        self.archived_at = now()

    def restore(self):
        self.archived_at = None

    objects = ArchivableQueryset.as_manager()
