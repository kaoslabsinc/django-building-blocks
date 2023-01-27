from django.db import models

_1_HOUR = 60 * 60
_24_HOURS = _1_HOUR * 24
_1_WEEK = _24_HOURS * 7
_30_DAYS = _24_HOURS * 30


class DynamicTimeRangeChoice(models.IntegerChoices):
    """Numbers are in seconds, as in seconds ago from now"""
    last_hour = _1_HOUR, "Last hour"
    last_24hrs = _24_HOURS, "Last 24 hours"
    last_week = _1_WEEK, "Last week"
    last_30days = _30_DAYS, "Last 30 days"


__all__ = (
    'DynamicTimeRangeChoice',
)
