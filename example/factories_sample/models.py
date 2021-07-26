from django.db import models

from building_blocks.models.factories import HasNameFactory, HasEmailFactory


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


class HasEmailExample(
    HasEmailFactory.as_abstract_model(),
    models.Model
):
    pass


class HasOptionalEmailExample(
    HasEmailFactory.as_abstract_model(optional=True),
    models.Model
):
    pass
