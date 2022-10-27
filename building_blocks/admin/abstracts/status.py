from building_blocks.consts.field_names import *
from ..blocks import BaseAdminBlock, FieldsetTitle


class HasStatusAdminBlock(BaseAdminBlock):
    list_display = (STATUS,)
    list_filter = (STATUS,)
    readonly_fields = (STATUS,)
    admin_fields = (STATUS,)
    the_admin_fieldset = (FieldsetTitle.admin, {'fields': admin_fields})


__all__ = (
    'HasStatusAdminBlock',
)
