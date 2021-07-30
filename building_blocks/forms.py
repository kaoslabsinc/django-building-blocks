from django import forms
from django.db import models
from django.db.models.base import ModelBase
from django.forms import modelform_factory


class UnrequiredFieldsForm(forms.Form):
    unrequired_fields = ()

    def __init__(self, *args, **kwargs):
        super(UnrequiredFieldsForm, self).__init__(*args, **kwargs)
        for field in self.unrequired_fields:
            if field in self.fields:
                self.fields[field].required = False


def unrequire_form(form_or_model: forms.Form or models.Model, unrequired_fields):
    _unreq_fields = unrequired_fields

    if isinstance(form_or_model, ModelBase):
        model = form_or_model
        form = modelform_factory(model, fields='__all__')
    else:
        form = form_or_model

    class UnrequiredModelForm(UnrequiredFieldsForm, form):
        unrequired_fields = _unreq_fields

    return UnrequiredModelForm
