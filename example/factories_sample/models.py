from django.db import models

from building_blocks.models.factories import HasNameFactory, HasEmailFactory, HasDescriptionFactory, \
    HasCoverPhotoFactory, HasIconFactory


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


class HasDescriptionExample(
    HasDescriptionFactory.as_abstract_model(),
    models.Model
):
    pass


class HasRequiredDescriptionExample(
    HasDescriptionFactory.as_abstract_model(required=True),
    models.Model
):
    pass


class HasCoverPhotoExample(
    HasCoverPhotoFactory.as_abstract_model(),
    models.Model
):
    pass


class HasRequiredCoverPhotoExample(
    HasCoverPhotoFactory.as_abstract_model(required=True),
    models.Model
):
    pass


class HasIconExample(
    HasIconFactory.as_abstract_model(),
    models.Model
):
    pass


class HasRequiredIconExample(
    HasIconFactory.as_abstract_model(required=True),
    models.Model
):
    pass
