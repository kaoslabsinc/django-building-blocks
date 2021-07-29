import pytest
from django.core.exceptions import ValidationError

from complex_factories_sample.models import HasAutoCodeGenerateFunctionExample

pytestmark = pytest.mark.django_db


def test_HasAutoCodeFactory():
    name = "name"
    obj = HasAutoCodeGenerateFunctionExample.objects.create(name=name)
    assert obj.code == "b068931cc450442b63f5b3d276ea4297"  # md5 hash of "name"


def test_HasAutoCodeFactory_unique():
    name = "name"
    HasAutoCodeGenerateFunctionExample.objects.create(name=name)
    with pytest.raises(ValidationError):
        HasAutoCodeGenerateFunctionExample.objects.create(name=name)
