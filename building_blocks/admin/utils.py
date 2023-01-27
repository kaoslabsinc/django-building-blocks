"""Set of utilities for `building_blocks.admin`"""

from typing import Sequence, Type

from building_blocks.admin.blocks.base import AdminBlock


def _combine_fields(attr, admin_block_classes: Sequence[Type['AdminBlock']]):
    """Return a combination of values stored in attribute `attr` for classes in `admin_block_classes`"""
    return tuple(
        field
        for cls in admin_block_classes if getattr(cls, attr) is not None
        for field in getattr(cls, attr)
    )


def combine_admin_blocks_factory(*admin_block_classes: Type['AdminBlock']):
    """
    Combine an arbitrary number of AdminBlock classes and return a composite class. Fields from the resulting class
    are a combination of fields from the consitutent classes

    :param admin_block_classes: spread argument with AdminBlock classes to be combined
    :return: combination of all classes in `admin_block_classes`
    """

    class XXXAdminBlock(*admin_block_classes, AdminBlock):
        base_fields = _combine_fields('base_fields', admin_block_classes)
        extra_fields = _combine_fields('extra_fields', admin_block_classes)
        admin_fields = _combine_fields('admin_fields', admin_block_classes)
        extra_admin_fields = _combine_fields('extra_admin_fields', admin_block_classes)
        actions = _combine_fields('actions', admin_block_classes)
        extra_actions = _combine_fields('extra_actions', admin_block_classes)
        list_display = _combine_fields('list_display', admin_block_classes)
        extra_list_display = _combine_fields('extra_list_display', admin_block_classes)
        list_filter = _combine_fields('list_filter', admin_block_classes)
        extra_list_filter = _combine_fields('extra_list_filter', admin_block_classes)
        readonly_fields = _combine_fields('readonly_fields', admin_block_classes)
        extra_readonly_fields = _combine_fields('extra_readonly_fields', admin_block_classes)
        edit_readonly_fields = _combine_fields('edit_readonly_fields', admin_block_classes)
        extra_edit_readonly_fields = _combine_fields('extra_edit_readonly_fields', admin_block_classes)
        autocomplete_fields = _combine_fields('autocomplete_fields', admin_block_classes)
        extra_autocomplete_fields = _combine_fields('extra_autocomplete_fields', admin_block_classes)
        search_fields = _combine_fields('search_fields', admin_block_classes)
        extra_search_fields = _combine_fields('extra_search_fields', admin_block_classes)

    cls_names = [cls.__name__.replace('AdminBlock', '') for cls in admin_block_classes]
    XXXAdminBlock.__name__ = XXXAdminBlock.__name__.replace('XXX', ''.join(cls_names))
    return XXXAdminBlock


def make_fieldset_collapsible(admin_fieldset):
    """
    Given an admin fieldset definition (just one fieldset/section), make it collapsible.

    :param admin_fieldset: one admin fieldset
    :return: the fieldset but collapsible
    """
    name, defs = admin_fieldset
    classes = defs.pop('classes', ())
    return name, {**defs, 'classes': (*classes, 'collapse')}


__all__ = (
    'combine_admin_blocks_factory',
    'make_fieldset_collapsible',
)
