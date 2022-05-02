from django.db import models
from django.utils.text import slugify


class NameSlugModelQuerySet(models.QuerySet):
    def get_or_create_by_name(self, name):
        return self.get_or_create(slug=slugify(name), defaults=dict(
            name=name
        ))
