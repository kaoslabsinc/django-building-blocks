from django.db import models
from django.db.models import Q


class ArchivableInterface:
    """Interface for Archivable objects"""
    is_archived: bool

    @property
    def is_available(self):
        return not self.is_archived

    def archive(self, *args, **kwargs):
        """
        Set the object as archived.
        """
        raise NotImplementedError

    def restore(self, *args, **kwargs):
        """
        Set the object as not archived (available).
        """
        raise NotImplementedError

    def unarchive(self, *args, **kwargs):
        """
        Set the object as not archived (available).
        """
        return self.restore(*args, **kwargs)


class ArchivableQuerySetInterface(models.QuerySet):
    """
    Default queryset interface for Archivable objects. Adds queryset methods to interact with the Archivable interface.
    """

    _Q_ARCHIVED: Q

    def archived(self):
        """
        :return: queryset with db rows that are archived
        """
        return self.filter(self._Q_ARCHIVED)

    def available(self):
        """
        :return: queryset with db rows that are "available" (aka not archived)
        """
        return self.exclude(self._Q_ARCHIVED)

    def set_archived(self):
        """
        Archive the objects in this queryset.

        :return: the return value from `.update()` i.e. the count of rows updated.
        """
        raise NotImplementedError

    def set_restored(self):
        """
        Restore (unarchive) the objects in this queryset.

        :return: the return value from `.update()` i.e. the count of rows updated.
        """
        raise NotImplementedError
