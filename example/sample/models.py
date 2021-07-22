from django.db import models

from building_blocks.models.abstracts import HasUUID, Archivable, Publishable
from building_blocks.models.mixins import HasInitials


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


class HasInitialsExample(
    HasInitials,
    models.Model
):
    take_initials_from = 'full_name'

    full_name = models.CharField(max_length=100)
