from django.db import models
from model_utils.models import TimeStampedModel

from .blocks import *


class UnnamedBaseKaosModel(
    HasUUIDModel,
    TimeStampedModel,
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
