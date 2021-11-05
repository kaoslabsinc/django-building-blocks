import uuid

from django.db import models
from django.utils.timezone import now

from .enums import PublishingStage
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

    archived_at = models.DateTimeField(null=True, blank=True)

    @property
    def is_active(self):
        return self.archived_at is None

    @property
    def archive_status(self):
        return 'archived' if self.archived_at else 'active'

    def archive(self):
        self.archived_at = now()
        return self

    def restore(self):
        self.archived_at = None
        return self

    objects = ArchivableQueryset.as_manager()


class Publishable(Archivable, models.Model):
    """
    Make the model have 3 stages of publication. Draft, Published and Archived.
    """
    class Meta:
        abstract = True

    published_at = models.DateTimeField(null=True, blank=True)
    first_published_at = models.DateTimeField(null=True, blank=True)

    @property
    def publishing_stage(self):
        if self.archived_at is None:
            if not self.published_at:
                return PublishingStage.draft
            else:
                return PublishingStage.published
        else:
            return PublishingStage.archived

    @property
    def is_active(self):
        return self.publishing_stage == PublishingStage.published

    def publish(self):
        assert self.publishing_stage == PublishingStage.draft, "Can only publish items in draft"
        right_now = now()
        if not self.first_published_at:
            self.first_published_at = right_now
        self.published_at = right_now
        return self

    def unpublish(self):
        assert self.publishing_stage == PublishingStage.published, "Can only unpublish items that are already published"
        self.published_at = None
        return self

    def restore(self, to_draft=True):
        assert self.publishing_stage == PublishingStage.archived, "Can only restore items in archive"
        if to_draft:
            self.published_at = None  # to set it to draft
        return super(Publishable, self).restore()

    objects = PublishableQueryset.as_manager()
