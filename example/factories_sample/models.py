from django.db import models

from building_blocks.models.factories import HasNameFactory


class HasNameExample(
    HasNameFactory.as_abstract_model(),
    models.Model
):
    pass


class HasOptionalNameExample(
    HasNameFactory.as_abstract_model(optional=True),
    models.Model
):
    pass
