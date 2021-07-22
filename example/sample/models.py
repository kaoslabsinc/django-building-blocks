from django.db import models

from building_blocks.abstracts import HasUUID, Archivable, Publishable


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


class PublishableHasUUID(
    HasUUID,
    Publishable,
    models.Model
):
    pass
