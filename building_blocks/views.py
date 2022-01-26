from django.contrib.auth.mixins import LoginRequiredMixin


class AjaxLoginRequiredMixin(LoginRequiredMixin):
    raise_exception = True
