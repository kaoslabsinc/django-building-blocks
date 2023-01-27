"""
Admin mixin enhancements
"""

from dj_kaos_utils.admin import EditReadonlyAdminMixin
from dj_kaos_utils.admin import PrepopulateSlugAdminMixin
from dj_kaos_utils.forms import unrequire_form

from building_blocks.consts.field_names import SLUG, NAME


class EnhancedHasSlugModelAdminMixin(EditReadonlyAdminMixin):
    """
    Admin mixin to make the slug field edit readonly

    :param edit_readonly_fields: (SLUG,)
    """
    edit_readonly_fields = (SLUG,)


class EnhancedSluggedKaosModelAdminMixin(
    PrepopulateSlugAdminMixin,
    EnhancedHasSlugModelAdminMixin
):
    """
    Admin mixin for SluggedModels so their slug is prepopulated from `slug_source` (by default `name`), slug field is
    marked as edit readonly and slug is unrequired in the from so to allow being auto set.

    :param slug_source: NAME
    """
    slug_source = NAME

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return unrequire_form(form, (SLUG,)) if not obj else form


__all__ = (
    'EnhancedHasSlugModelAdminMixin',
    'EnhancedSluggedKaosModelAdminMixin',
)
