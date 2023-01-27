"""
Model admins for Kaos Models
"""

from django.contrib import admin

from building_blocks.consts.field_names import UUID, NAME, SLUG
from .base import *
from .mixins import EnhancedSluggedKaosModelAdminMixin


class KaosModelAdmin(BaseKaosModelAdmin, admin.ModelAdmin):
    """
    Model admin for `KaosModel`

    :param search_fields: (UUID, NAME)
    :param list_display: (NAME,)
    """
    search_fields = (UUID, NAME)
    list_display = (NAME,)


class KaosModelAdminExtra(BaseKaosModelAdminExtra, KaosModelAdmin):
    """
    `KaosModelAdmin` with extra admin fields (modified)

    :param fieldsets: ((None, {'fields': (('name',),)}), ('Admin', {'fields': ('uuid', 'created', 'modified')}))
    """


class BasicSluggedKaosModelAdmin(BaseBasicSluggedKaosModelAdmin, KaosModelAdmin):
    """
    Model admin for `SluggedKaosModel`

    :param search_fields: (UUID, SLUG, NAME)
    :param list_display_extra: (SLUG,)
    """
    search_fields = (UUID, SLUG, NAME)
    list_display_extra = (SLUG,)


class BasicSluggedKaosModelAdminExtra(BaseBasicSluggedKaosModelAdminExtra, BasicSluggedKaosModelAdmin):
    """
    `BasicSluggedKaosModelAdmin` with extra admin fields (modified)
    """


class SluggedKaosModelAdmin(EnhancedSluggedKaosModelAdminMixin, BasicSluggedKaosModelAdmin):
    """
    BasicSluggedKaosModelAdmin enhanced with `EnhancedSluggedKaosModelAdminMixin`
    """


class SluggedKaosModelAdminExtra(EnhancedSluggedKaosModelAdminMixin, BasicSluggedKaosModelAdminExtra):
    """
    BasicSluggedKaosModelAdminExtra enhanced with `EnhancedSluggedKaosModelAdminMixin` (with extra admin fields
    (modified))
    """
