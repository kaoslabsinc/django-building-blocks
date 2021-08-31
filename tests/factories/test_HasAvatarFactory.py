from django import forms

from factories_sample.models import HasAvatarExample


class HasAvatarModelForm(forms.ModelForm):
    class Meta:
        model = HasAvatarExample
        fields = '__all__'


def test_HasAvatarFactory():
    avatar = "path/to/avatar.jpg"
    obj = HasAvatarExample(avatar=avatar)
    assert obj.avatar == avatar


def test_HasAvatarFactory_no_avatar():
    obj = HasAvatarExample()
    form = HasAvatarModelForm(data={}, instance=obj)
    assert form.is_valid()
