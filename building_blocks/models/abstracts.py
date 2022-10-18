from django.contrib import admin
from django.db import models
from django_fsm import FSMIntegerField, transition

from .enums import ArchiveStatus
from .interfaces import ArchivableInterface
from .querysets import ArchivableQuerySet, StatusArchivableQuerySet


class Archivable(ArchivableInterface, models.Model):
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
    @admin.display(boolean=True)
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
            assert self.is_archived is True, f"{self} is not archived"
        self.is_archived = False


class HasStatus(models.Model):
    status = FSMIntegerField(default=0)

    class Meta:
        abstract = True


class StatusArchivable(
    ArchivableInterface,
    HasStatus,
    models.Model
):
    status = FSMIntegerField(choices=ArchiveStatus.choices, default=ArchiveStatus.available)

    @property
    def is_archived(self):
        return self.status == ArchiveStatus.archived

    @transition(status, target=ArchiveStatus.archived)
    def archive(self):
        pass

    @transition(status, source=ArchiveStatus.archived, target=ArchiveStatus.archived)
    def restore(self):
        pass

    objects = StatusArchivableQuerySet.as_manager()

    class Meta:
        abstract = True


__all__ = [
    'Archivable',
    'HasStatus',
    'StatusArchivable',
]
