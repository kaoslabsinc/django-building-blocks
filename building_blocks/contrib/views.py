from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import RedirectView


class AjaxLoginRequiredMixin(LoginRequiredMixin):
    raise_exception = True


class AdminRedirectView(RedirectView):
    model = None
    lookup_field = 'uuid'

    def get_redirect_url(self, *args, **kwargs):
        opts = self.model._meta
        obj = get_object_or_404(self.model, **{self.lookup_field: kwargs[self.lookup_field]})
        admin_url_pattern = f'admin:{opts.app_label}_{opts.model_name}_change'
        return reverse(admin_url_pattern, args=(obj.id,))
