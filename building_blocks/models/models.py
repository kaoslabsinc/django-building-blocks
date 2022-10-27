from rules.contrib.models import RulesModel

from .base import *
from .blocks import *
from .blocks import TitledModel


class KaosModel(
    BaseKaosModel,
    RulesModel
):
    """
    Abstract Base Model that comes with UUID, create and modified, and name fields. Powered up by django-rules through
    `RulesModel`.
    """

    class Meta:
        abstract = True


class UnnamedKaosModel(
    UnnamedBaseKaosModel,
    RulesModel,
):
    """
    Abstract Base Model that comes with UUID, create and modified fields. Powered up by django-rules through
    `RulesModel`. Cousin of KaosModel but without the name field.
    """

    class Meta:
        abstract = True


class TitledKaosModel(
    TitledModel,
    UnnamedKaosModel
):
    class Meta:
        abstract = True


class SluggedKaosModel(
    SluggedModel,
    KaosModel
):
    """
    `KaosModel` with slug.
    """
    slug_source = 'name'

    class Meta:
        abstract = True


__all__ = [
    'KaosModel',
    'UnnamedKaosModel',
    'TitledKaosModel',
    'SluggedKaosModel',
]
