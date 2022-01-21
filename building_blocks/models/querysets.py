from django.db import models

from .enums import ArchiveStatus, PublishingStatus


class ArchivableQueryset(models.QuerySet):
    def active(self):
        return self.filter(status=ArchiveStatus.active)

    def archived(self):
        return self.filter(status=ArchiveStatus.archived)


class PublishableQueryset(ArchivableQueryset):
    def draft(self):
        return self.filter(status=PublishingStatus.draft)

    def published(self):
        return self.filter(status=PublishingStatus.published)

    def active(self):
        return self.published()
