from django.db import models


class ArchivableQuerySet(models.QuerySet):
    """
    Default queryset interface for Archivable objects. Adds queryset methods to interact with the Archivable interface.
    """
    def available(self):
        """
        :return: queryset with db rows that are "available" (aka not archived)
        """
        return self.filter(is_archived=False)

    def archived(self):
        """
        :return: queryset with db rows that are archived
        """
        return self.filter(is_archived=True)

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


__all__ = [
    'ArchivableQuerySet',
]
