from django.db import models


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
