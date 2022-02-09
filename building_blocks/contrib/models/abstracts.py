from django.db import models

from building_blocks.factories import HasNameFactory, HasAutoSlugFactory
from .querysets import NameSlugModelQuerySet


class NameSlugModel(
    HasNameFactory.as_abstract_model(),
    HasAutoSlugFactory.as_abstract_model('name'),
    models.Model
):
    class Meta:
        abstract = True

    objects = NameSlugModelQuerySet.as_manager()


__all__ = [
    'NameSlugModel',
]
