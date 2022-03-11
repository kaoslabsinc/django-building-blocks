from django.db import models
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView

__all__ = [
    'QSFiltersViewSetMixin',
]


class QSFiltersViewSetMixin(GenericAPIView):

    def get_queryset(self):
        qs: models.QuerySet = super(QSFiltersViewSetMixin, self).get_queryset()

        if qs_method := self.request.query_params.get('qs'):
            try:
                qs = getattr(qs, qs_method)(user=self.request.user)
            except AttributeError:
                raise ValidationError({'qs': f"{qs_method} is not a valid choice"})

        return qs
