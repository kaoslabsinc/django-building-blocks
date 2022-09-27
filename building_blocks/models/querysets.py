from django.db import models


class ArchivableQuerySet(models.QuerySet):
    def available(self):
        return self.filter(is_archived=False)

    def archived(self):
        return self.filter(is_archived=True)


__all__ = [
    'ArchivableQuerySet',
]
