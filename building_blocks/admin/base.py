from django.contrib.admin.options import BaseModelAdmin

from .blocks import *
from .mixins import EnhancedSluggedKaosModelAdminMixin


class BaseKaosModelAdmin(BaseModelAdmin):
    readonly_fields = KaosModelAdminBlock.readonly_fields
    fieldsets = (
        (None, {'fields': (KaosModelAdminBlock.base_fields,)}),
        KaosModelAdminBlock.the_admin_fieldset,
    )


class BaseKaosModelAdminExtra(BaseKaosModelAdmin):
    fieldsets = (
        *BaseKaosModelAdmin.fieldsets[:-1],
        KaosModelAdminBlock.the_admin_fieldset_extra,
    )


class BaseBasicSluggedKaosModelAdmin(BaseKaosModelAdmin):
    fieldsets = (
        *BaseKaosModelAdmin.fieldsets[:-1],
        SluggedKaosModelAdminBlock.the_admin_fieldset,
    )


class BaseBasicSluggedKaosModelAdminExtra(BaseKaosModelAdmin):
    fieldsets = (
        *BaseBasicSluggedKaosModelAdmin.fieldsets[:-1],
        SluggedKaosModelAdminBlock.the_admin_fieldset_extra,
    )


class BaseSluggedKaosModelAdmin(EnhancedSluggedKaosModelAdminMixin, BaseBasicSluggedKaosModelAdmin):
    pass


class BaseSluggedKaosModelAdminExtra(EnhancedSluggedKaosModelAdminMixin, BaseBasicSluggedKaosModelAdminExtra):
    pass


__all__ = (
    'BaseKaosModelAdmin',
    'BaseKaosModelAdminExtra',
    'BaseBasicSluggedKaosModelAdmin',
    'BaseBasicSluggedKaosModelAdminExtra',
    'BaseSluggedKaosModelAdmin',
    'BaseSluggedKaosModelAdminExtra',
)
