from django.db import models
from django.utils.text import slugify

from .enums import ArchiveStatus, PublishingStatus


class HasStatusQuerySet(models.QuerySet):
    @staticmethod
    def _transform_status_kwarg(kwargs):
        status = kwargs.pop('status', None)
        if status is not None:
            kwargs['_status'] = status
        return kwargs

    def filter(self, *args, **kwargs):
        kwargs = self._transform_status_kwarg(kwargs)
        return super(HasStatusQuerySet, self).filter(*args, **kwargs)


class ArchivableQuerySet(HasStatusQuerySet):
    def active(self):
        return self.filter(status=ArchiveStatus.active)

    def archived(self):
        return self.filter(status=ArchiveStatus.archived)


class PublishableQuerySet(ArchivableQuerySet):
    def draft(self):
        return self.filter(status=PublishingStatus.draft)

    def published(self):
        return self.filter(status=PublishingStatus.published)

    def active(self):
        return self.published()


class NameSlugModelQuerySet(models.QuerySet):
    def get_or_create_by_name(self, name):
        return self.get_or_create(slug=slugify(name), defaults=dict(
            name=name
        ))
