from django import forms

from building_blocks.forms import unrequire_form


def test_unrequire_form():
    class MyForm(forms.Form):
        name = forms.CharField()

    my_form = MyForm()
    assert not my_form.is_valid()

    my_form = MyForm(data={'name': "Name"})
    assert my_form.is_valid()

    NewMyForm = unrequire_form(MyForm, ('name',))
    new_my_form = NewMyForm(data={})
    assert new_my_form.is_valid()

    new_my_form = NewMyForm(data={'name': "Name"})
    assert new_my_form.is_valid()
