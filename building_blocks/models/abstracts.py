import uuid

from django.db import models
from django.utils.timezone import now
from django_fsm import FSMField, transition, RETURN_VALUE

from .enums import ArchiveStatus, PublishingStatus
from .querysets import ArchivableQueryset, PublishableQueryset


class HasUUID(models.Model):
    """
    Add a unique UUID field to the model
    """

    class Meta:
        abstract = True

    uuid = models.UUIDField(verbose_name="UUID", unique=True, default=uuid.uuid4, editable=False)

    @property
    def uuid_str(self):
        return str(self.uuid)

    @property
    def shortcode(self):
        return self.uuid_str.split('-')[0]


class Archivable(models.Model):
    """
    Make the model be archivable, ie objects can be archived to go out of rotation without deleting them from the
    database
    """

    class Meta:
        abstract = True

    status = FSMField(choices=ArchiveStatus.choices, default=ArchiveStatus.active)

    @property
    def is_active(self):
        return self.status == ArchiveStatus.active

    @transition(field=status, source='+', target=PublishingStatus.archived)
    def archive(self):
        pass

    @transition(field=status, source=ArchiveStatus.archived, target=ArchiveStatus.active)
    def restore(self):
        pass

    objects = ArchivableQueryset.as_manager()


class Publishable(Archivable, models.Model):
    """
    Make the model have 3 stages of publication. Draft, Published and Archived.
    """

    class Meta:
        abstract = True

    status = FSMField(choices=PublishingStatus.choices, default=PublishingStatus.draft)
    first_published_at = models.DateTimeField(null=True, blank=True)

    @property
    def is_active(self):
        return self.status == PublishingStatus.published

    @transition(field=status, source=PublishingStatus.draft, target=PublishingStatus.published)
    def publish(self):
        if not self.first_published_at:
            self.first_published_at = now()

    @transition(field=status, source=PublishingStatus.published, target=PublishingStatus.draft)
    def unpublish(self):
        pass

    @transition(field=status,
                source=PublishingStatus.archived,
                target=RETURN_VALUE(PublishingStatus.draft, PublishingStatus.published))
    def restore(self, to_draft=True):
        return PublishingStatus.draft if to_draft else PublishingStatus.published

    objects = PublishableQueryset.as_manager()


class Orderable(models.Model):
    DEFAULT_ORDER = 99999
    order = models.PositiveIntegerField(default=DEFAULT_ORDER)

    class Meta:
        ordering = ('order', 'id')
        abstract = True
