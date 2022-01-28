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
