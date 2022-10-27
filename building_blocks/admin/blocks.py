from building_blocks.admin.utils import experimental_combine_admin_blocks_factory
from building_blocks.consts.field_names import *


class FieldsetTitle:
    admin = "Admin"


class BaseAdminBlock:
    base_fields = None
    extra_fields = None
    admin_fields = None
    extra_admin_fields = None
    the_fieldset = None
    the_fieldset_extra = None
    the_admin_fieldset = None
    the_admin_fieldset_extra = None

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
    the_admin_fieldset = (FieldsetTitle.admin, {'fields': admin_fields})


class HasSlugBaseAdminBlock(BaseAdminBlock):
    admin_fields = (SLUG,)
    the_admin_fieldset = (FieldsetTitle.admin, {'fields': admin_fields})


class TimeStampedBaseAdminBlock(BaseAdminBlock):
    readonly_fields = (CREATED, MODIFIED)
    admin_fields = (CREATED,)
    extra_admin_fields = (MODIFIED,)
    the_admin_fieldset = (FieldsetTitle.admin, {'fields': admin_fields})
    the_admin_fieldset_extra = (FieldsetTitle.admin, {'fields': admin_fields + extra_admin_fields})


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
