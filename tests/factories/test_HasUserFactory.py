import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from complex_factories_sample.models import HasUserExample, HasOptionalUserExample, HasOneToOneUserExample

User = get_user_model()
pytestmark = pytest.mark.django_db


def test_HasUserFactory():
    username = "test"
    user = User.objects.create(username=username)
    obj = HasUserExample.objects.create(user=user)
    assert obj.user.username == username


def test_HasUserFactory_no_user():
    with pytest.raises(IntegrityError):
        HasUserExample.objects.create()


def test_HasUserFactory_optional_user():
    HasOptionalUserExample.objects.create()


def test_HasUserFactory_onetoone():
    user = User.objects.create(username="test")
    HasOneToOneUserExample.objects.create(user=user)
    with pytest.raises(IntegrityError):
        HasOneToOneUserExample.objects.create(user=user)
