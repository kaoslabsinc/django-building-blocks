from django import forms

from factories_sample.models import HasEmailExample, HasOptionalEmailExample


class HasEmailModelForm(forms.ModelForm):
    class Meta:
        model = HasEmailExample
        fields = '__all__'


class HasOptionalEmailModelForm(forms.ModelForm):
    class Meta:
        model = HasOptionalEmailExample
        fields = '__all__'


def test_HasEmailFactory():
    email = "email@example.com"
    obj = HasEmailExample(email=email)
    assert obj.email == email


def test_HasEmailFactory_no_email():
    obj = HasEmailExample()
    form = HasEmailModelForm(data={}, instance=obj)
    assert not form.is_valid()


def test_HasEmailFactory_optional_email():
    obj = HasOptionalEmailExample()
    form = HasOptionalEmailModelForm(data={}, instance=obj)
    assert form.is_valid()
