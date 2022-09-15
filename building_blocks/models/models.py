from rules.contrib.models import RulesModel

from .base import *


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


__all__ = [
    'KaosModel',
    'UnnamedKaosModel',
]
