from django import forms

from factories_sample.models import HasNameExample, HasOptionalNameExample


class HasNameModelForm(forms.ModelForm):
    class Meta:
        model = HasNameExample
        fields = '__all__'


class HasOptionalNameModelForm(forms.ModelForm):
    class Meta:
        model = HasOptionalNameExample
        fields = '__all__'


def test_HasNameFactory():
    name = "name"
    obj = HasNameExample(name=name)
    assert obj.name == name


def test_HasNameFactory_no_name():
    obj = HasNameExample()
    form = HasNameModelForm(data={}, instance=obj)
    assert not form.is_valid()


def test_HasNameFactory_optional_name():
    obj = HasOptionalNameExample()
    form = HasOptionalNameModelForm(data={}, instance=obj)
    assert form.is_valid()
