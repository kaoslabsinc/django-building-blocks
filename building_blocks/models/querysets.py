from django.db import models


class ArchivableQuerySet(models.QuerySet):
    def available(self):
        return self.filter(is_archived=False)

    def archived(self):
        return self.filter(is_archived=True)

    def set_archived(self):
        return self.update(is_archived=True)

    def set_restored(self):
        return self.update(is_archived=False)


__all__ = [
    'ArchivableQuerySet',
]
