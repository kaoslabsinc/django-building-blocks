from django.db import models


class ArchiveStatus(models.IntegerChoices):
    available = 100
    archived = -1


class PublishStatus(models.IntegerChoices):
    draft = 0
    published = 100
    archived = ArchiveStatus.archived
