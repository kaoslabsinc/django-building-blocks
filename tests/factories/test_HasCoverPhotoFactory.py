from django import forms

from factories_sample.models import HasCoverPhotoExample, HasRequiredCoverPhotoExample


class HasCoverPhotoModelForm(forms.ModelForm):
    class Meta:
        model = HasCoverPhotoExample
        fields = '__all__'


class HasRequiredCoverPhotoModelForm(forms.ModelForm):
    class Meta:
        model = HasRequiredCoverPhotoExample
        fields = '__all__'


def test_HasCoverPhotoFactory():
    cover_photo = "path/to/cover_photo"
    obj = HasCoverPhotoExample(cover_photo=cover_photo)
    assert obj.cover_photo == cover_photo


def test_HasCoverPhotoFactory_no_cover_photo():
    obj = HasCoverPhotoExample()
    form = HasCoverPhotoModelForm(data={}, instance=obj)
    assert form.is_valid()


def test_HasCoverPhotoFactory_required_cover_photo():
    obj = HasRequiredCoverPhotoExample()
    form = HasRequiredCoverPhotoModelForm(data={}, instance=obj)
    assert not form.is_valid()
