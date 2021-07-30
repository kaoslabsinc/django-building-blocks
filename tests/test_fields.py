import pytest

from sample.models import LowerCaseCharFieldExample

pytestmark = pytest.mark.django_db


def test_LowerCaseCharField():
    name = "TEsT"
    LowerCaseCharFieldExample.objects.create(lc_field=name)
    obj = LowerCaseCharFieldExample.objects.get()
    assert obj.lc_field == "test"


def test_LowerCaseCharField_query():
    name = "TEsT"
    LowerCaseCharFieldExample.objects.create(lc_field=name)
    assert LowerCaseCharFieldExample.objects.filter(lc_field="TesT")
