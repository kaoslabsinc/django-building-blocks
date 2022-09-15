from building_blocks.models import HasUUIDModel
from building_blocks.models.mixins import NamedModel
from django.db import models


class UnnamedBaseKaosModel(
    TimeStampedModel,
    HasUUIDModel,
    models.Model,
):
    class Meta:
        abstract = True


class BaseKaosModel(
    NamedModel,
    UnnamedBaseKaosModel,
):
    class Meta:
        abstract = True


__all__ = [
    'UnnamedBaseKaosModel',
    'BaseKaosModel',
]
