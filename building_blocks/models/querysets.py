from django.db import models
from django.db.models import Q

from .enums import PublishingStage


class ArchivableQueryset(models.QuerySet):
    _Q_IS_ACTIVE = Q(archived_at__isnull=True)

    def active(self):
        return self.filter(ArchivableQueryset._Q_IS_ACTIVE)

    def archived(self):
        return self.filter(~ArchivableQueryset._Q_IS_ACTIVE)


class PublishableQueryset(ArchivableQueryset):
    def draft(self):
        return ArchivableQueryset.active(self).filter(published_at__isnull=True)

    def published(self):
        return ArchivableQueryset.active(self).filter(published_at__isnull=False)

    def active(self):
        return self.published()
