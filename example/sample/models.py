from django.db import models

from building_blocks.abstracts import HasUUID, Archivable


class HasUUIDExample(
    HasUUID,
    models.Model
):
    pass


class ArchivableHasUUID(
    HasUUID,
    Archivable,
    models.Model
):
    pass
