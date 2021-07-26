from django import forms

from factories_sample.models import HasIconExample, HasRequiredIconExample


class HasIconModelForm(forms.ModelForm):
    class Meta:
        model = HasIconExample
        fields = '__all__'


class HasRequiredIconModelForm(forms.ModelForm):
    class Meta:
        model = HasRequiredIconExample
        fields = '__all__'


def test_HasIconFactory():
    icon = "path/to/icon"
    obj = HasIconExample(icon=icon)
    assert obj.icon == icon


def test_HasIconFactory_no_icon():
    obj = HasIconExample()
    form = HasIconModelForm(data={}, instance=obj)
    assert form.is_valid()


def test_HasIconFactory_required_icon():
    obj = HasRequiredIconExample()
    form = HasRequiredIconModelForm(data={}, instance=obj)
    assert not form.is_valid()
