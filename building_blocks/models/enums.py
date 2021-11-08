from django.db import models


class ArchiveStatus(models.TextChoices):
    active = 'active'
    archived = 'archived'


class PublishingStatus(models.TextChoices):
    draft = 'draft'
    published = 'published'
    archived = ArchiveStatus.archived
