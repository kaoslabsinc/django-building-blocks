from dj_kaos_utils.admin import EditReadonlyAdminMixin

from building_blocks.admin import PrepopulateSlugAdminMixin
from building_blocks.consts.field_names import *


class EnhancedHasSlugModelAdminMixin(EditReadonlyAdminMixin):
    edit_readonly_fields = (SLUG,)


class EnhancedSluggedKaosModelAdminMixin(
    PrepopulateSlugAdminMixin,
    EnhancedHasSlugModelAdminMixin
):
    slug_source = NAME


__all__ = (
    'EnhancedHasSlugModelAdminMixin',
    'EnhancedSluggedKaosModelAdminMixin',
)
