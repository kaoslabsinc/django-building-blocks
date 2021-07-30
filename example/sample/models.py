from django.db import models

from building_blocks.models import HasInitials
from building_blocks.models import HasUUID, Archivable, Publishable
from building_blocks.models.mixins import HasAutoFields


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


class HasAutoFieldsExample(
    HasAutoFields,
    models.Model
):
    name = models.CharField(max_length=100)
    name_upper = models.CharField(max_length=100)

    def set_auto_fields(self):
        if not self.name_upper:
            self.name_upper = self.name.upper()


class TimeStampedExample(
    models.Model
):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
