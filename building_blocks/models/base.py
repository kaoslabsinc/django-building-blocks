from django.db import models
from model_utils.models import TimeStampedModel

from .mixins import *


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
