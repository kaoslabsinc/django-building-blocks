from django.db import models


class TwoPlacesDecimalField(models.DecimalField):
    description = "A DecimalField with 2 decimal places"

    def __init__(self, *args, **kwargs):
        kwargs['max_digits'] = kwargs.get('max_digits', 10)
        kwargs['decimal_places'] = 2
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_digits']
        del kwargs['decimal_places']
        return name, path, args, kwargs


class MoneyField(TwoPlacesDecimalField):
    description = "An amount of money"


class CaseInsensitiveFieldMixin:
    """
    Field mixin that uses case-insensitive lookup alternatives if they exist.
    """
    LOOKUP_CONVERSIONS = {
        'exact': 'iexact',
        'contains': 'icontains',
        'startswith': 'istartswith',
        'endswith': 'iendswith',
        'regex': 'iregex',
    }

    def get_lookup(self, lookup_name):
        converted = self.LOOKUP_CONVERSIONS.get(lookup_name, lookup_name)
        return super().get_lookup(converted)


class ToLowerCaseFieldMixin:
    """
    Always save a field as lowercase
    """

    def to_python(self, value):
        return super(ToLowerCaseFieldMixin, self).to_python(value).lower()


class LowerCaseCharField(ToLowerCaseFieldMixin, CaseInsensitiveFieldMixin, models.CharField):
    pass
