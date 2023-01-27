from typing import Sequence, Optional

from building_blocks.consts.field_names import *


class AdminFieldsetTitle:
    """
    Class to hold constant values for django fieldset titles

    :param admin: "Admin"
    :param extra: "Extra"
    """
    admin = "Admin"
    extra = "Extra"


class AdminBlockMeta(type):
    base_fields: Optional[Sequence[str]]
    extra_fields: Optional[Sequence[str]]
    admin_fields: Optional[Sequence[str]]
    extra_admin_fields: Optional[Sequence[str]]

    @property
    def the_fieldset(cls):
        if cls.base_fields is not None:
            return None, {'fields': cls.base_fields}

    @property
    def the_fieldset_extra(cls):
        if cls.base_fields is not None:
            return AdminFieldsetTitle.extra, {'fields': cls.extra_fields}

    @property
    def the_admin_fieldset(cls):
        if cls.admin_fields is not None:
            return AdminFieldsetTitle.admin, {'fields': cls.admin_fields}

    @property
    def the_admin_fieldset_extra(cls):
        if cls.extra_admin_fields is not None:
            admin_fields = cls.admin_fields or ()
            return AdminFieldsetTitle.admin, {'fields': (*admin_fields, *cls.extra_admin_fields)}


class BaseAdminBlock(metaclass=AdminBlockMeta):
    """
    BaseAdminBlock is the base class for creating custom admin blocks. It provides a set of fields and methods that can
    be overridden and extended to create custom behavior and appearance for the admin interface.

    Corresponds to `django.contrib.admin.BaseModelAdmin`.

    :param base_fields: A list of fields to be displayed in the admin interface.
    :param extra_fields: A list of extra/optional fields to be displayed in the admin interface.
    :param admin_fields: fields that should be always included in the admin fieldset
    :param extra_admin_fields: extra/optional fields that should be always included in the admin fieldset
    :param readonly_fields: fields that should be always readonly in the admin form
    :param extra_readonly_fields: fields that should be readonly in the admin form, but optionally
    :param edit_readonly_fields: fields that should be always readonly in the admin form when editing an existing object
    :param extra_edit_readonly_fields: fields that should be readonly in the admin form when editing an existing object,
        but optionally
    :param autocomplete_fields: fields that should use autocomplete widgets in the admin form
    :param extra_autocomplete_fields: fields that should use autocomplete widgets in the admin form, but optionally
    """

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
    """
    AdminBlock is used to configure views for the admin interface. It inherits from BaseAdminBlock and contains fields
    for django admin list view config.

    Corresponds to `django.contrib.admin.ModelAdmin`. Usually contains config for list views over `BaseAdminBlock`

    :param actions: A list of predefined actions that can be performed on selected objects in the admin list view.
    :param extra_actions: A list of extra/optional actions that can be performed on selected objects in the admin list
        view.
    :param search_fields: A list of fields to be searched when the user enters a search query in the admin list view.
    :param extra_search_fields: A list of extra/optional fields to be searched when the user enters a search query in
        the admin list view.
    :param list_display: A list of fields to be displayed in the admin list view.
    :param extra_list_display: A list of extra/optional fields to be displayed in the admin list view.
    :param list_filter: A list of fields to be used as filters in the admin list view.
    :param extra_list_filter: A list of extra/optional fields to be used as filters in the admin list view.
    """

    actions = None
    extra_actions = None
    search_fields = None
    extra_search_fields = None
    list_display = None
    extra_list_display = None
    list_filter = None
    extra_list_filter = None


class HasUUIDAdminBlock(AdminBlock):
    """
    AdminBlock for models extending `building_blocks.models.blocks.HasUUID`

    :param readonly_fields: (UUID,)
    :param admin_fields: (UUID,)
    """
    readonly_fields = (UUID,)
    admin_fields = (UUID,)


class HasSlugAdminBlock(AdminBlock):
    """
    AdminBlock for models with a `slug` field

    :param admin_fields: (SLUG,)
    :param edit_readonly_fields: (SLUG,)
    """
    admin_fields = (SLUG,)
    edit_readonly_fields = (SLUG,)


class TimeStampedAdminBlock(AdminBlock):
    """
    AdminBlock for models extending `TimeStampedModel`

    :param readonly_fields: (CREATED, MODIFIED)
    :param admin_fields: (CREATED,)
    :param extra_admin_fields: (MODIFIED,)
    """
    readonly_fields = (CREATED, MODIFIED)
    admin_fields = (CREATED,)
    extra_admin_fields = (MODIFIED,)


__all__ = (
    'AdminFieldsetTitle',
    'BaseAdminBlock',
    'AdminBlock',
    'HasUUIDAdminBlock',
    'HasSlugAdminBlock',
    'TimeStampedAdminBlock',
)
