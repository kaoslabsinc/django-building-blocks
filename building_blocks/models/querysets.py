from django.db import models

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


def _get_obj_keys_tuple(obj, lookup_fields):
    return tuple(getattr(obj, field) for field in lookup_fields)


def _get_filter_dict(objs, lookup_fields):
    return {
        field + '__in': [
            getattr(obj, field)
            for obj in objs
        ]
        for field in lookup_fields
    }


class BulkUpdateCreateQuerySet(models.QuerySet):
    def bulk_update_or_create(self, objs, lookup_fields, update_fields):
        """
        Creates or updates in bulk a list of objects

        :param objs: List of objects
        :param lookup_fields: Name of field that unique identifies the objects
        :param update_fields: List of fields to update
        :return:
        """
        if not isinstance(lookup_fields, tuple):
            lookup_fields = (lookup_fields,)

        existing = {
            _get_obj_keys_tuple(obj, lookup_fields): obj
            for obj in self.filter(**_get_filter_dict(objs, lookup_fields))
        }
        bulk_create = []
        bulk_update = []
        for obj in objs:
            lookup_tuple = _get_obj_keys_tuple(obj, lookup_fields)
            if lookup_tuple in existing:
                existing_obj = existing[lookup_tuple]
                for field in update_fields:
                    setattr(existing_obj, field, getattr(obj, field))
                bulk_update.append(existing_obj)
            else:
                bulk_create.append(obj)
        self.bulk_create(bulk_create)
        self.bulk_update(bulk_update, update_fields)
        # Rerunning the queryset to make sure all instances returned have ids. The values in created are pointers to
        # instances before they have their id
        return self.filter(**_get_filter_dict(objs, lookup_fields))


__all__ = [
    'HasStatusQuerySet',
    'ArchivableQuerySet',
    'PublishableQuerySet',
    'BulkUpdateCreateQuerySet',
]
