from django.contrib import admin

from building_blocks.admin.mixins import EnhancedSluggedKaosModelAdminMixin
from building_blocks.consts.field_names import *
from .base import *


class KaosModelAdmin(BaseKaosModelAdmin, admin.ModelAdmin):
    search_fields = (UUID, NAME)
    list_display = (NAME,)


class KaosModelAdminExtra(BaseKaosModelAdminExtra, KaosModelAdmin):
    pass


class BasicSluggedKaosModelAdmin(BaseBasicSluggedKaosModelAdmin, KaosModelAdmin):
    search_fields = (UUID, SLUG, NAME)
    list_display_extra = (SLUG,)


class BasicSluggedKaosModelAdminExtra(BaseBasicSluggedKaosModelAdminExtra, BasicSluggedKaosModelAdmin):
    pass


class SluggedKaosModelAdmin(EnhancedSluggedKaosModelAdminMixin, BasicSluggedKaosModelAdmin):
    pass


class SluggedKaosModelAdminExtra(EnhancedSluggedKaosModelAdminMixin, BasicSluggedKaosModelAdminExtra):
    pass
