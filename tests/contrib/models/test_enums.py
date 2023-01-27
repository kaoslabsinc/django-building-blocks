from building_blocks.contrib.models import DynamicTimeRangeChoice


class TestDynamicTimeRangeChoice:
    def test_choices(self):
        assert DynamicTimeRangeChoice.choices == [
            (DynamicTimeRangeChoice.last_hour.value, DynamicTimeRangeChoice.last_hour.label),
            (DynamicTimeRangeChoice.last_24hrs.value, DynamicTimeRangeChoice.last_24hrs.label),
            (DynamicTimeRangeChoice.last_week.value, DynamicTimeRangeChoice.last_week.label),
            (DynamicTimeRangeChoice.last_30days.value, DynamicTimeRangeChoice.last_30days.label),
        ]

    def test_last_hour(self):
        assert DynamicTimeRangeChoice.last_hour == 3600
        assert DynamicTimeRangeChoice.last_hour.label == "Last hour"

    def test_last_24hrs(self):
        assert DynamicTimeRangeChoice.last_24hrs == 3600 * 24
        assert DynamicTimeRangeChoice.last_24hrs.label == "Last 24 hours"

    def test_last_week(self):
        assert DynamicTimeRangeChoice.last_week == 3600 * 24 * 7
        assert DynamicTimeRangeChoice.last_week.label == "Last week"

    def test_last_30days(self):
        assert DynamicTimeRangeChoice.last_30days == 3600 * 24 * 30
        assert DynamicTimeRangeChoice.last_30days.label == "Last 30 days"
