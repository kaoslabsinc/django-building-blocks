from django.db import models


class DynamicTimeRangeChoice(models.IntegerChoices):
    """Numbers are in seconds, as in seconds ago from now"""
    last_hour = 60 * 60
    last_24hrs = 24 * last_hour
    last_week = 7 * last_24hrs
    last_30days = 30 * last_24hrs


__all__ = (
    'DynamicTimeRangeChoice',
)
