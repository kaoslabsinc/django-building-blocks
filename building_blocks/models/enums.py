from django.db import models


class ArchiveStatus(models.IntegerChoices):
    active = 100
    archived = -1


class PublishingStatus(models.IntegerChoices):
    draft = 0
    published = 100
    archived = -1
