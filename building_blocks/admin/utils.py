from typing import Sequence, Type

from building_blocks.admin import BaseAdminBlock


def _combine_fields(attr, admin_block_classes: Sequence[Type[BaseAdminBlock]]):
    return tuple(
        field
        for cls in admin_block_classes if getattr(cls, attr) is not None
        for field in getattr(cls, attr)
    )


def combine_admin_blocks_factory(*admin_block_classes: Type[BaseAdminBlock]):
    class XXXAdminBlock(*admin_block_classes):
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
    name, defs = admin_fieldset
    classes = defs.pop('classes', ())
    return name, {**defs, 'classes': (*classes, 'collapse')}


__all__ = (
    'combine_admin_blocks_factory',
    'make_fieldset_collapsible',
)
