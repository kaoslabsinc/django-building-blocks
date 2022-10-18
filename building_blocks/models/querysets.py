from django.db import models
from django.db.models import Q

from .enums import ArchiveStatus, PublishStatus
from .interfaces import ArchivableQuerySetInterface


class ArchivableQuerySet(
    ArchivableQuerySetInterface,
    models.QuerySet
):
    _Q_ARCHIVED = Q(is_archived=True)

    def set_archived(self):
        return self.update(is_archived=True)

    def set_restored(self):
        return self.update(is_archived=False)


class StatusArchivableQuerySet(
    ArchivableQuerySetInterface,
    models.QuerySet
):
    _Q_ARCHIVED = Q(status=ArchiveStatus.archived)

    def set_archived(self):
        return self.update(status=ArchiveStatus.archived)

    def set_restored(self):
        return self.update(status=ArchiveStatus.available)


class PublishableQuerySet(
    StatusArchivableQuerySet,
    models.QuerySet
):
    _Q_PUBLISHED = Q(status=PublishStatus.published)

    def published(self):
        return self.filter(self._Q_PUBLISHED)

    def set_restored(self):
        return self.update(status=PublishStatus.draft)

    def set_published(self):
        return self.update(status=PublishStatus.published)

    def set_unpublished(self):
        return self.update(status=PublishStatus.draft)


__all__ = [
    'ArchivableQuerySet',
    'StatusArchivableQuerySet',
    'PublishableQuerySet',
]
