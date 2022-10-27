from django.contrib import admin

from building_blocks.consts.field_names import *
from .base import *
from .mixins import EnhancedSluggedKaosModelAdminMixin


class KaosModelAdmin(BaseKaosModelAdmin, admin.ModelAdmin):
    search_fields = (UUID, NAME)
    list_display = (NAME,)


class KaosModelAdminExtra(BaseKaosModelAdminExtra, KaosModelAdmin):
    pass


class SluggedKaosModelAdmin(BaseSluggedKaosModelAdmin, KaosModelAdmin):
    search_fields = (UUID, SLUG, NAME)
    list_display_extra = (SLUG,)


class SluggedKaosModelAdminExtra(BaseSluggedKaosModelAdminExtra, SluggedKaosModelAdmin):
    pass


class EnhancedSluggedKaosModelAdmin(EnhancedSluggedKaosModelAdminMixin, SluggedKaosModelAdmin):
    pass


class EnhancedSluggedKaosModelAdminExtra(EnhancedSluggedKaosModelAdminMixin, SluggedKaosModelAdminExtra):
    pass
