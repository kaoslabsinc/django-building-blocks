from django.db import models

from building_blocks.fields import LowerCaseCharField
from building_blocks.models import HasInitials
from building_blocks.models import HasUUID, Archivable, Publishable
from building_blocks.models.factories import HasNameFactory, HasEmailFactory
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


def default_json():
    return {
        'field': 'value',
        'field2': 'value2',
    }


class AdminUtilsExample(
    models.Model
):
    json = models.JSONField(default=default_json)
    url = models.URLField()
    image_url = models.URLField()


class Container(
    HasNameFactory.as_abstract_model(),
    models.Model
):
    pass


class ContainerItem(
    HasNameFactory.as_abstract_model(),
    HasEmailFactory.as_abstract_model(optional=True),
    models.Model
):
    container = models.ForeignKey(Container, on_delete=models.PROTECT)


class LowerCaseCharFieldExample(models.Model):
    lc_field = LowerCaseCharField(max_length=100)
