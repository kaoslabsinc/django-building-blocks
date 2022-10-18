from django.db import models


class ArchiveStatus(models.IntegerChoices):
    available = 100
    archived = -1
