from django.db import models


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
