from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

from building_blocks.models.mixins import HasAutoFields
from .utils import generate_field_kwargs


class AbstractModelFactory:
    @staticmethod
    def as_abstract_model(**kwargs):
        raise NotImplementedError

    @staticmethod
    def _get_fk_params(one_to_one, optional, on_delete):
        fk_field_cls = models.OneToOneField if one_to_one else models.ForeignKey
        on_delete = on_delete or (models.PROTECT if not optional else models.SET_NULL)
        return fk_field_cls, on_delete


class HasNameFactory(AbstractModelFactory):
    @staticmethod
    def as_abstract_model(optional=False, **kwargs):
        class HasName(models.Model):
            class Meta:
                abstract = True

            name = models.CharField(max_length=255, blank=optional, **kwargs)

            def __str__(self):
                return self.name if self.name else super(HasName, self).__str__()

        return HasName


class HasEmailFactory(AbstractModelFactory):
    @staticmethod
    def as_abstract_model(optional=False, **kwargs):
        class HasEmail(models.Model):
            class Meta:
                abstract = True

            email = models.EmailField(blank=optional, **kwargs)

        return HasEmail


class HasDescriptionFactory(AbstractModelFactory):
    @staticmethod
    def as_abstract_model(required=False, **kwargs):
        class HasDescription(models.Model):
            class Meta:
                abstract = True

            description = models.TextField(blank=not required, **kwargs)

        return HasDescription


class HasCoverPhotoFactory(AbstractModelFactory):
    @staticmethod
    def as_abstract_model(upload_to='', required=False, **kwargs):
        class HasCoverPhoto(models.Model):
            class Meta:
                abstract = True

            cover_photo = models.ImageField(upload_to=upload_to, blank=not required, **kwargs)

        return HasCoverPhoto


class HasIconFactory(AbstractModelFactory):
    @staticmethod
    def as_abstract_model(upload_to='', required=False, **kwargs):
        class HasIcon(models.Model):
            class Meta:
                abstract = True

            icon = models.ImageField(upload_to=upload_to, blank=not required, **kwargs)

        return HasIcon


class HasUserFactory(AbstractModelFactory):
    @staticmethod
    def as_abstract_model(related_name=None, one_to_one=False, optional=False, on_delete=None, **kwargs):
        user_field_cls, on_delete = AbstractModelFactory._get_fk_params(one_to_one, optional, on_delete)

        class HasUser(models.Model):
            class Meta:
                abstract = True

            user = user_field_cls(settings.AUTH_USER_MODEL, on_delete=on_delete, related_name=related_name,
                                  **generate_field_kwargs(optional_null=optional), **kwargs)

        return HasUser


class HasAutoCodeFactory(AbstractModelFactory):
    """
    The child model has to define a field denoted by `auto_code_field`. This field will be autoset at the time of
    creation of the model by either using the output from the generate function
    (f`def generate_{auto_code_field}(self):`) or by `slugify`ing the field denoted by `source_field`. The code has to
    be unique for the inherited model.
    """

    @staticmethod
    def generate_code(instance, auto_code_field, source_field):
        generate_func = getattr(instance, 'generate_' + auto_code_field, None)
        if generate_func:
            return generate_func()
        else:
            return slugify(getattr(instance, source_field))

    @staticmethod
    def as_abstract_model(auto_code_field, source_field=None):
        class HasAutoCode(HasAutoFields, models.Model):
            class Meta:
                abstract = True

            def set_auto_fields(self):
                super(HasAutoCode, self).set_auto_fields()
                if not getattr(self, auto_code_field, None):
                    code = HasAutoCodeFactory.generate_code(self, auto_code_field, source_field)
                    if type(self)._default_manager.filter(**{auto_code_field: code}).exists():
                        raise ValidationError(
                            f"{type(self)._meta.verbose_name.capitalize()} with this {auto_code_field} already exists")
                    setattr(self, auto_code_field, code)

        return HasAutoCode


class HasAutoSlugFactory(AbstractModelFactory):
    """
    The child model will automatically get assigned a slug, by either using the output of `def generate_slug(self)` or
    by `slugify`ing the field denoted by `source_field`.
    """

    @staticmethod
    def as_abstract_model(source_field=None, **kwargs):
        class HasAutoSlug(
            HasAutoCodeFactory.as_abstract_model('slug', source_field),
            models.Model
        ):
            class Meta:
                abstract = True

            slug = models.SlugField(max_length=255, unique=True, **kwargs)

        return HasAutoSlug


class HasAvatarFactory(AbstractModelFactory):
    @staticmethod
    def as_abstract_model(upload_to='', required=False, **kwargs):
        class HasAvatar(models.Model):
            class Meta:
                abstract = True

            avatar = models.ImageField(upload_to=upload_to, blank=not required, **kwargs)

        return HasAvatar


__all__ = [
    'AbstractModelFactory',
    'HasNameFactory',
    'HasEmailFactory',
    'HasDescriptionFactory',
    'HasCoverPhotoFactory',
    'HasIconFactory',
    'HasUserFactory',
    'HasAutoCodeFactory',
    'HasAutoSlugFactory',
    'HasAvatarFactory',
]
