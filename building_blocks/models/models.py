from rules.contrib.models import RulesModel

from .base import *


class KaosModel(
    BaseKaosModel,
    RulesModel
):
    class Meta:
        abstract = True


class UnnamedKaosModel(
    UnnamedBaseKaosModel,
    RulesModel,
):
    class Meta:
        abstract = True


__all__ = [
    'KaosModel',
    'UnnamedKaosModel',
]
