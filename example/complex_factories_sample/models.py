import hashlib

from django.db import models

from building_blocks.models.factories import HasUserFactory, HasNameFactory, HasAutoCodeFactory, HasAutoSlugFactory


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


class HasAutoCodeGenerateFunctionExample(
    HasNameFactory.as_abstract_model(),
    HasAutoCodeFactory.as_abstract_model('code'),
    models.Model
):
    code = models.CharField(max_length=255)

    def generate_code(self):
        return hashlib.md5(self.name.encode()).hexdigest()


class HasAutoSlugExample(
    HasNameFactory.as_abstract_model(),
    HasAutoSlugFactory.as_abstract_model(source_field='name'),
    models.Model
):
    pass
