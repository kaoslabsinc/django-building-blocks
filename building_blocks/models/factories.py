from django.contrib.auth import get_user_model
from django.db import models

from .utils import generate_field_kwargs


class AbstractModelFactory:
    @staticmethod
    def as_abstract_model(**kwargs):
        raise NotImplementedError


class HasNameFactory(AbstractModelFactory):
    @staticmethod
    def as_abstract_model(optional=False):
        class HasName(models.Model):
            class Meta:
                abstract = True

            name = models.CharField(max_length=255, blank=optional)

            def __str__(self):
                return self.name if self.name else super(HasName, self).__str__()

        return HasName


class HasEmailFactory(AbstractModelFactory):
    @staticmethod
    def as_abstract_model(optional=False):
        class HasEmail(models.Model):
            class Meta:
                abstract = True

            email = models.EmailField(blank=optional)

        return HasEmail


class HasDescriptionFactory(AbstractModelFactory):
    @staticmethod
    def as_abstract_model(required=False):
        class HasDescription(models.Model):
            class Meta:
                abstract = True

            description = models.TextField(blank=not required)

        return HasDescription


class HasCoverPhotoFactory(AbstractModelFactory):
    @staticmethod
    def as_abstract_model(upload_to='', required=False):
        class HasCoverPhoto(models.Model):
            class Meta:
                abstract = True

            cover_photo = models.ImageField(upload_to=upload_to, blank=not required)

        return HasCoverPhoto


class HasIconFactory(AbstractModelFactory):
    @staticmethod
    def as_abstract_model(upload_to='', required=False):
        class HasIcon(models.Model):
            class Meta:
                abstract = True

            icon = models.ImageField(upload_to=upload_to, blank=not required)

        return HasIcon


User = get_user_model()


class HasUserFactory(AbstractModelFactory):
    @staticmethod
    def as_abstract_model(related_name, one_to_one=False, optional=False):
        user_field_cls = models.OneToOneField if one_to_one else models.ForeignKey

        class HasUser(models.Model):
            class Meta:
                abstract = True

            user = user_field_cls(User, on_delete=models.PROTECT,
                                  related_name=related_name,
                                  **generate_field_kwargs(optional_null=optional))

        return HasUser
