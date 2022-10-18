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
    _Q_DRAFT = Q(status=PublishStatus.draft)

    def published(self):
        """
        :return: queryset with db rows that are published
        """
        return self.filter(self._Q_PUBLISHED)

    def draft(self):
        """
        :return: queryset with db rows that are in draft
        """
        return self.filter(self._Q_DRAFT)

    def set_restored(self):
        return self.update(status=PublishStatus.draft)

    def set_published(self):
        """
        Publish the objects in this queryset.

        :return: the return value from `.update()` i.e. the count of rows updated.
        """
        return self.update(status=PublishStatus.published)

    def set_unpublished(self):
        """
        Unpublish the objects (set to draft) in this queryset.

        :return: the return value from `.update()` i.e. the count of rows updated.
        """
        return self.update(status=PublishStatus.draft)


__all__ = [
    'ArchivableQuerySet',
    'StatusArchivableQuerySet',
    'PublishableQuerySet',
]
