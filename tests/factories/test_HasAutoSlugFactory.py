import pytest
from django.core.exceptions import ValidationError

from complex_factories_sample.models import HasAutoSlugExample

pytestmark = pytest.mark.django_db


def test_HasAutoSlugFactory():
    name = "My name"
    obj = HasAutoSlugExample.objects.create(name=name)
    assert obj.slug == "my-name"


def test_HasAutoSlugFactory_unique():
    name = "name"
    HasAutoSlugExample.objects.create(name=name)
    with pytest.raises(ValidationError):
        HasAutoSlugExample.objects.create(name=name)
