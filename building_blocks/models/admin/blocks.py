from building_blocks.consts.field_names import *


class FieldsetTitle:
    admin = "Admin"


class BaseAdminBlock:
    base_fields = ()
    extra_fields = None
    admin_fields = ()
    extra_admin_fields = None
    the_fieldset = None
    the_fieldset_extra = None
    the_admin_fieldset = None
    the_admin_fieldset_extra = None


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
        *HasUUIDBaseAdminBlock.base_fields,
        *TimeStampedBaseAdminBlock.base_fields,
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
    'BaseAdminBlock',
    'HasUUIDBaseAdminBlock',
    'HasSlugBaseAdminBlock',
    'TimeStampedBaseAdminBlock',
    'UnnamedKaosBaseAdminBlock',
    'KaosModelAdminBlock',
    'SluggedKaosModelAdminBlock',
)
