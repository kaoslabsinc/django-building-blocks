from django.db import models

from .enums import DynamicTimeRangeChoice


class DynamicTimeRangeField(models.PositiveIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = kwargs.get('choices', DynamicTimeRangeChoice.choices)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if kwargs.get('choices') == DynamicTimeRangeChoice.choices:
            del kwargs['choices']
        return name, path, args, kwargs


__all__ = (
    'DynamicTimeRangeField',
)
