from django.db import models
from django.db.models import Q

from .enums import PublishingStage


class ArchivableQueryset(models.QuerySet):
    _Q_IS_ACTIVE = Q(archived_at__isnull=True)

    def active(self):
        return self.filter(ArchivableQueryset._Q_IS_ACTIVE)

    def archived(self):
        return self.filter(~ArchivableQueryset._Q_IS_ACTIVE)


class PublishableQueryset(models.QuerySet):
    def draft(self):
        return self.filter(publishing_stage=PublishingStage.draft)

    def published(self):
        return self.filter(publishing_stage=PublishingStage.published)

    active = published

    def archived(self):
        return self.filter(publishing_stage=PublishingStage.archived)
