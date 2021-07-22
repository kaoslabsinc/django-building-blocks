from django.db import models
from django.db.models import Q


class ArchivableQueryset(models.QuerySet):
    _Q_IS_ACTIVE = Q(archived_at__isnull=True)

    def active(self):
        return self.filter(ArchivableQueryset._Q_IS_ACTIVE)

    def archived(self):
        return self.filter(~ArchivableQueryset._Q_IS_ACTIVE)
