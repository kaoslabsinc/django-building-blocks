from django.db import models
from django.db.models import Q

from .enums import ArchiveStatus
from .interfaces import ArchivableQuerySetInterface


class ArchivableQuerySet(
    ArchivableQuerySetInterface,
    models.QuerySet
):
    """
    Default queryset interface for Archivable objects. Adds queryset methods to interact with the Archivable interface.
    """
    _Q_ARCHIVED = Q(is_archived=True)

    def set_archived(self):
        """
        Archive the objects in this queryset.

        :return: the return value from `.update()` i.e. the count of rows updated.
        """
        return self.update(is_archived=True)

    def set_restored(self):
        """
        Restore (unarchive) the objects in this queryset.

        :return: the return value from `.update()` i.e. the count of rows updated.
        """
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


__all__ = [
    'ArchivableQuerySet',
    'StatusArchivableQuerySet',
]
