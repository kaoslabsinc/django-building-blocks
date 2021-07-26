from django.db import models

from building_blocks.models.factories import HasUserFactory


class HasUserExample(
    HasUserFactory.as_abstract_model(related_name='+'),
    models.Model
):
    pass


class HasOptionalUserExample(
    HasUserFactory.as_abstract_model(related_name='+', optional=True),
    models.Model
):
    pass


class HasOneToOneUserExample(
    HasUserFactory.as_abstract_model(related_name='+', one_to_one=True),
    models.Model
):
    pass


class HasOptionalOneToOneUserExample(
    HasUserFactory.as_abstract_model(related_name='+', optional=True, one_to_one=True),
    models.Model
):
    pass
