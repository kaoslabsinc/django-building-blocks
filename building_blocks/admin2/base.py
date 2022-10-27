from django.contrib.admin.options import BaseModelAdmin

from .blocks import *
from .mixins import EnhancedSluggedKaosModelAdminMixin


class BaseKaosModelAdmin(BaseModelAdmin):
    fieldsets = (
        (None, {'fields': (KaosModelAdminBlock.base_fields,)}),
        KaosModelAdminBlock.the_admin_fieldset,
    )


class BaseKaosModelAdminExtra(BaseKaosModelAdmin):
    fieldsets = (
        *BaseKaosModelAdmin.fieldsets[:-1],
        KaosModelAdminBlock.the_admin_fieldset_extra,
    )


class BaseSluggedKaosModelAdmin(BaseKaosModelAdmin):
    fieldsets = (
        *BaseKaosModelAdmin.fieldsets[:-1],
        SluggedKaosModelAdminBlock.the_admin_fieldset,
    )


class BaseSluggedKaosModelAdminExtra(BaseKaosModelAdmin):
    fieldsets = (
        *BaseSluggedKaosModelAdmin.fieldsets[:-1],
        SluggedKaosModelAdminBlock.the_admin_fieldset_extra,
    )


class BaseEnhancedSluggedKaosModelAdmin(EnhancedSluggedKaosModelAdminMixin, BaseSluggedKaosModelAdmin):
    pass


class BaseEnhancedSluggedKaosModelAdminExtra(EnhancedSluggedKaosModelAdminMixin, BaseSluggedKaosModelAdminExtra):
    pass


__all__ = (
    'BaseKaosModelAdmin',
    'BaseKaosModelAdminExtra',
    'BaseSluggedKaosModelAdmin',
    'BaseSluggedKaosModelAdminExtra',
    'BaseEnhancedSluggedKaosModelAdmin',
    'BaseEnhancedSluggedKaosModelAdminExtra',
)
