from collections import OrderedDict

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

__all__ = [
    'NameSlugSerializer',
    'UUIDLookupSerializerMixin',
    'WritableNestedModelSerializerMixin',
]


class NameSlugSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name', 'slug',
        )
        lookup_field = 'slug'


class UUIDLookupSerializerMixin:
    class Meta:
        fields = (
            'uuid',
        )
        lookup_field = 'uuid'
        extra_kwargs = {
            'url': {'lookup_field': 'uuid'}
        }


class WritableNestedModelSerializerMixin(serializers.HyperlinkedModelSerializer):
    lookup_field = None
    create_if_not_exists = False

    def __init__(self, *args, **kwargs):
        self.lookup_field = kwargs.pop('lookup_field', self.lookup_field) or getattr(self.Meta, 'lookup_field', None)
        self.create_if_not_exists = kwargs.pop('create_if_not_exists', self.create_if_not_exists)
        super().__init__(*args, **kwargs)

    def get_object(self, key_value):
        model_class = self.Meta.model
        return model_class.objects.get(**{self.lookup_field: key_value})

    def to_internal_value(self, data):
        assert self.lookup_field is not None, "You should specify lookup_field"
        model_class = self.Meta.model
        errors = OrderedDict()
        if key_data := data.get(self.lookup_field):
            key_value = self.fields[self.lookup_field].to_internal_value(key_data)
            try:
                return self.get_object(key_value)
            except model_class.DoesNotExist:
                if self.create_if_not_exists:
                    return self.create({self.lookup_field: key_value})
                else:
                    errors[self.lookup_field] = f"object with {self.lookup_field} '{key_value}' doesn't exist."
        else:
            errors[self.lookup_field] = f"You should specify the {self.lookup_field} for this object."
        if errors:
            raise ValidationError(errors)
