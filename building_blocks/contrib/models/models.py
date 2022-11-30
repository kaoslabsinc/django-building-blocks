import uuid
from copy import copy
from datetime import timedelta

from django.db import models
from django.utils.functional import cached_property
from django.utils.timezone import now

from .fields import DynamicTimeRangeField


class HasTimeRangeModel(models.Model):
    class Meta:
        abstract = True

    _time_range_dynamic = DynamicTimeRangeField(null=True, blank=True)
    _time_range_start = models.DateTimeField(null=True, blank=True)
    _time_range_end = models.DateTimeField(null=True, blank=True)

    @cached_property
    def time_range__start(self):
        if self._time_range_start:
            return self._time_range_start
        if self._time_range_dynamic is not None:
            return now() - timedelta(seconds=self._time_range_dynamic)

    @property
    def time_range__end(self):
        if self._time_range_end:
            return self._time_range_end


class DuplicableModel(models.Model):
    class Meta:
        abstract = True

    def _duplicate_pre_save(self, *args, **kwargs):
        new = copy(self)
        if getattr(new, 'id', None) is not None:
            new.id = None
        if getattr(new, 'uuid', None) is not None:
            new.uuid = uuid.uuid4()
        if getattr(new, 'slug', None) is not None:
            new.slug = None
        if getattr(self, 'name', None) is not None:
            new.name = self.name + " (copy)"
        for arg in args:
            setattr(new, arg, None)
        for key, val in kwargs.items():
            setattr(new, key, val)
        return new

    def duplicate(self, *args, **kwargs):
        new = self._duplicate_pre_save()
        new.save()
        return new


__all__ = (
    'HasTimeRangeModel',
    'DuplicableModel',
)
