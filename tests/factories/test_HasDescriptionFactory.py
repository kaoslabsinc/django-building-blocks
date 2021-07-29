from django import forms

from factories_sample.models import HasDescriptionExample, HasRequiredDescriptionExample


class HasDescriptionModelForm(forms.ModelForm):
    class Meta:
        model = HasDescriptionExample
        fields = '__all__'


class HasRequiredDescriptionModelForm(forms.ModelForm):
    class Meta:
        model = HasRequiredDescriptionExample
        fields = '__all__'


def test_HasDescriptionFactory():
    description = "description"
    obj = HasDescriptionExample(description=description)
    assert obj.description == description


def test_HasDescriptionFactory_no_description():
    obj = HasDescriptionExample()
    form = HasDescriptionModelForm(data={}, instance=obj)
    assert form.is_valid()


def test_HasDescriptionFactory_required_description():
    obj = HasRequiredDescriptionExample()
    form = HasRequiredDescriptionModelForm(data={}, instance=obj)
    assert not form.is_valid()
