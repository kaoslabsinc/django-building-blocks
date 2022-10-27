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


class UnnamedKaosBaseAdminBlock(HasUUIDBaseAdminBlock, TimeStampedBaseAdminBlock):
    readonly_fields = (
        *HasUUIDBaseAdminBlock.readonly_fields,
        *TimeStampedBaseAdminBlock.readonly_fields,
    )
    admin_fields = (
        *HasUUIDBaseAdminBlock.admin_fields,
        *TimeStampedBaseAdminBlock.admin_fields,
    )
    extra_admin_fields = TimeStampedBaseAdminBlock.extra_admin_fields
    the_admin_fieldset = (FieldsetTitle.admin, {'fields': admin_fields})
    the_admin_fieldset_extra = (FieldsetTitle.admin, {'fields': admin_fields + extra_admin_fields})


class KaosModelAdminBlock(UnnamedKaosBaseAdminBlock):
    base_fields = (
        NAME,
    )
    the_fieldset = (None, {'fields': base_fields})


class SluggedKaosModelAdminBlock(HasSlugBaseAdminBlock, UnnamedKaosBaseAdminBlock):
    admin_fields = (
        *HasSlugBaseAdminBlock.admin_fields,
        *UnnamedKaosBaseAdminBlock.admin_fields,
    )
    the_admin_fieldset = (FieldsetTitle.admin, {'fields': admin_fields})
    the_admin_fieldset_extra = (FieldsetTitle.admin, {'fields': (*admin_fields,
                                                                 *UnnamedKaosBaseAdminBlock.extra_admin_fields)})


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
