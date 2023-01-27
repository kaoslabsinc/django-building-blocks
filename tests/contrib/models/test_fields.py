import pytest

from building_blocks.contrib.models import DynamicTimeRangeChoice, DynamicTimeRangeField


class TestDynamicTimeRangeField:
    @pytest.fixture
    def instance(self):
        return DynamicTimeRangeField()

    @pytest.fixture
    def instance_custom(self):
        return DynamicTimeRangeField(choices=())

    def test_choices(self, instance):
        assert instance.choices == DynamicTimeRangeChoice.choices

    def test_choices_custom(self, instance_custom):
        assert instance_custom.choices == ()

    def test_deconstruct(self, instance):
        assert instance.deconstruct() == (None, 'building_blocks.contrib.models.fields.DynamicTimeRangeField', [], {})
