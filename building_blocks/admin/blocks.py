from typing import Sequence

from building_blocks.admin.utils import experimental_combine_admin_blocks_factory
from building_blocks.consts.field_names import *


class FieldsetTitle:
    admin = "Admin"
    extra = "Extra"


class AdminBlockMeta(type):
    base_fields: Sequence[str] | None
    extra_fields: Sequence[str] | None
    admin_fields: Sequence[str] | None
    extra_admin_fields: Sequence[str] | None

    @property
    def the_fieldset(cls):
        if cls.base_fields is not None:
            return None, {'fields': cls.base_fields}

    @property
    def the_fieldset_extra(cls):
        if cls.base_fields is not None:
            return FieldsetTitle.extra, {'fields': cls.extra_fields}

    @property
    def the_admin_fieldset(cls):
        if cls.admin_fields is not None:
            return FieldsetTitle.admin, {'fields': cls.admin_fields}

    @property
    def the_admin_fieldset_extra(cls):
        if cls.extra_admin_fields is not None:
            admin_fields = cls.admin_fields or ()
            return FieldsetTitle.admin, {'fields': (*admin_fields, *cls.extra_admin_fields)}


class BaseAdminBlock(metaclass=AdminBlockMeta):
    base_fields = None
    extra_fields = None
    admin_fields = None
    extra_admin_fields = None

    actions = None
    extra_actions = None
    list_display = None
    extra_list_display = None
    list_filter = None
    extra_list_filter = None
    readonly_fields = None
    extra_readonly_fields = None
    edit_readonly_fields = None
    extra_edit_readonly_fields = None
    autocomplete_fields = None
    extra_autocomplete_fields = None
    search_fields = None
    extra_search_fields = None


class HasUUIDBaseAdminBlock(BaseAdminBlock):
    readonly_fields = (UUID,)
    admin_fields = (UUID,)


class HasSlugBaseAdminBlock(BaseAdminBlock):
    admin_fields = (SLUG,)


class TimeStampedBaseAdminBlock(BaseAdminBlock):
    readonly_fields = (CREATED, MODIFIED)
    admin_fields = (CREATED,)
    extra_admin_fields = (MODIFIED,)


UnnamedKaosBaseAdminBlock = experimental_combine_admin_blocks_factory(
    HasUUIDBaseAdminBlock,
    TimeStampedBaseAdminBlock
)


class KaosModelAdminBlock(UnnamedKaosBaseAdminBlock):
    base_fields = (
        NAME,
    )
    the_fieldset = (None, {'fields': base_fields})


SluggedKaosModelAdminBlock = experimental_combine_admin_blocks_factory(
    HasSlugBaseAdminBlock,
    UnnamedKaosBaseAdminBlock
)

__all__ = (
    'FieldsetTitle',
    'BaseAdminBlock',
    'HasUUIDBaseAdminBlock',
    'HasSlugBaseAdminBlock',
    'TimeStampedBaseAdminBlock',
    'UnnamedKaosBaseAdminBlock',
    'KaosModelAdminBlock',
    'SluggedKaosModelAdminBlock',
)
