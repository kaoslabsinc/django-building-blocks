from django.db import models

from .querysets import ArchivableQuerySet


class Archivable(models.Model):
    """
    Provides and interface to create archivable (or soft deletable) models. If you don't want to delete an instance from
    your DB, but want to mark it inactive use this abstract model.
    Filter for available (i.e. not archived) objects using the queryset method .available(). It is provided through the
    model's objects manager.
    """

    class Meta:
        abstract = True

    is_archived = models.BooleanField(default=False)

    objects = ArchivableQuerySet.as_manager()

    @property
    def is_available(self):
        return not self.is_archived

    def archive(self, force=False):
        """
        Set the object as archived.

        :param force: By default, the method checks if the object is archived and will through an error if it is. Set
            `force` to True to disable this check.
        """
        if not force:
            assert self.is_archived is False, f"{self} is already archived"
        self.is_archived = True

    def restore(self, force=False):
        """
        Set the object as not archived (available).

        :param force: By default, the method checks if the object is not archived and will through an error if it is.
            Set `force` to True to disable this check.
        """

        if not force:
            assert self.is_archived is False, f"{self} is not archived"
        self.is_archived = False


__all__ = [
    'Archivable',
]
