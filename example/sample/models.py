from django.db import models

from building_blocks.abstracts import HasUUID


class HasUUIDExample(
    HasUUID,
    models.Model
):
    pass
