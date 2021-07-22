from django.db import models


class PublishingStage(models.TextChoices):
    draft = 'draft'
    published = 'published'
    archived = 'archived'
