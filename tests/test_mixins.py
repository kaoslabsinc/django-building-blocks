import pytest

from sample.models import HasInitialsExample, HasAutoFieldsExample


def test_HasInitials():
    instance = HasInitialsExample(full_name="Example Name")
    assert instance.initials == "EN"


def test_HasInitials_attribute_missing():
    instance = HasInitialsExample(full_name="Example Name")
    instance.take_initials_from = None
    with pytest.raises(AttributeError):
        instance.initials  # NoQA


def test_HasAutoFields():
    instance = HasAutoFieldsExample(name="Example Name")
    instance.clean()
    assert instance.name_upper == "EXAMPLE NAME"
