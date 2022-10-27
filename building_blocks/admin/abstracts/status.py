from building_blocks.consts.field_names import *
from ..blocks import AdminBlock


class HasStatusAdminBlock(AdminBlock):
    list_display = (STATUS,)
    list_filter = (STATUS,)
    readonly_fields = (STATUS,)
    admin_fields = (STATUS,)


__all__ = (
    'HasStatusAdminBlock',
)
