from dj_kaos_utils.admin import EditReadonlyAdminMixin
from dj_kaos_utils.forms import unrequire_form

from dj_kaos_utils.admin import PrepopulateSlugAdminMixin
from building_blocks.consts.field_names import *


class EnhancedHasSlugModelAdminMixin(EditReadonlyAdminMixin):
    edit_readonly_fields = (SLUG,)


class EnhancedSluggedKaosModelAdminMixin(
    PrepopulateSlugAdminMixin,
    EnhancedHasSlugModelAdminMixin
):
    slug_source = NAME

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return unrequire_form(form, ('slug',)) if not obj else form


__all__ = (
    'EnhancedHasSlugModelAdminMixin',
    'EnhancedSluggedKaosModelAdminMixin',
)
