import pytest

from building_blocks.contrib.models import HasVisualizationInterface


class TestHasVisualizationInterface:
    @pytest.fixture
    def instance(self):
        return HasVisualizationInterface()

    def test_visualize_not_implemented(self, instance):
        with pytest.raises(NotImplementedError):
            instance.visualize()
