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

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

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

    def restore(self):
        self.archived_at = None

    objects = ArchivableQueryset.as_manager()


class Publishable(models.Model):
    """
    Make the model have 3 stages of publication. Draft, Published and Archived.
    """
    class Meta:
        abstract = True

    publishing_stage = models.CharField(max_length=30, choices=PublishingStage.choices, default=PublishingStage.draft)
    publishing_stage_changed_at = models.DateTimeField(null=True, blank=True)

    @property
    def is_active(self):
        return self.publishing_stage == PublishingStage.published

    def publish(self):
        assert self.publishing_stage == PublishingStage.draft, "Can only publish items in draft"
        self.publishing_stage = PublishingStage.published
        self.publishing_stage_changed_at = now()

    def unpublish(self):
        assert self.publishing_stage == PublishingStage.published, "Can only unpublish items that are already published"
        self.publishing_stage = PublishingStage.draft
        self.publishing_stage_changed_at = now()

    def archive(self):
        self.publishing_stage = PublishingStage.archived
        self.publishing_stage_changed_at = now()

    def restore(self):
        assert self.publishing_stage == PublishingStage.archived, "Can only restore items in archive"
        self.publishing_stage = PublishingStage.draft
        self.publishing_stage_changed_at = now()

    objects = PublishableQueryset.as_manager()
