from typing import Type

from dj_kaos_utils.admin.utils import get_admin_link
from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import path, include
from django.urls import reverse, NoReverseMatch
from django.views.generic import RedirectView


class AdminDetailRedirectView(RedirectView):
    model = None
    lookup_field = 'uuid'

    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(self.model, **{self.lookup_field: kwargs[self.lookup_field]})
        return get_admin_link(obj)


class AdminCreateRedirectView(RedirectView):
    model: Type[models.Model] = None

    def get_redirect_url(self, *args, **kwargs):
        opts = self.model._meta
        try:
            return reverse(f'admin:{opts.app_label}_{opts.model_name}_add')
        except NoReverseMatch:
            return None


def build_admin_redirect_urls(model):
    return path('admin-redirect/', include((
        [
            path(
                'create/',
                AdminCreateRedirectView.as_view(model=model),
                name='create'
            ),
            path(
                '<uuid:uuid>/',
                AdminDetailRedirectView.as_view(model=model),
                name='detail'
            ),
        ],
        'admin-redirect'
    )))


__all__ = (
    'AdminDetailRedirectView',
    'AdminCreateRedirectView',
    'build_admin_redirect_urls',
)
