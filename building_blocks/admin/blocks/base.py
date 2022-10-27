from typing import Sequence

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
    readonly_fields = None
    extra_readonly_fields = None
    edit_readonly_fields = None
    extra_edit_readonly_fields = None
    autocomplete_fields = None
    extra_autocomplete_fields = None


class AdminBlock(BaseAdminBlock):
    actions = None
    extra_actions = None
    search_fields = None
    extra_search_fields = None
    list_display = None
    extra_list_display = None
    list_filter = None
    extra_list_filter = None


class HasUUIDAdminBlock(AdminBlock):
    readonly_fields = (UUID,)
    admin_fields = (UUID,)


class HasSlugAdminBlock(AdminBlock):
    admin_fields = (SLUG,)


class TimeStampedAdminBlock(AdminBlock):
    readonly_fields = (CREATED, MODIFIED)
    admin_fields = (CREATED,)
    extra_admin_fields = (MODIFIED,)


__all__ = (
    'FieldsetTitle',
    'BaseAdminBlock',
    'AdminBlock',
    'HasUUIDAdminBlock',
    'HasSlugAdminBlock',
    'TimeStampedAdminBlock',
)
