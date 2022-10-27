from dj_kaos_utils.admin import EditReadonlyAdminMixin
from dj_kaos_utils.admin import PrepopulateSlugAdminMixin
from dj_kaos_utils.admin.utils import render_anchor
from dj_kaos_utils.forms import unrequire_form
from django.contrib import admin

from building_blocks.consts.field_names import *


class WithLinkDisplayAdminMixin:
    """
    Add a `link_display` admin display method to show a certain url as a link.
    """
    link_field = None
    link_content = "🔗 Link"

    list_display = ('link_display',)
    readonly_fields = ('link_display',)
    fields = ('link_display',)

    def get_link_url(self, obj):
        if self.link_field:
            return getattr(obj, self.link_field)

    def get_link_content(self, obj):
        if self.link_content is None:
            return self.get_link_url(obj)
        return self.link_content

    @admin.display(description="link")
    def link_display(self, obj):
        if link_url := self.get_link_url(obj):
            return render_anchor(link_url, self.get_link_content(obj))


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
    'WithLinkDisplayAdminMixin',
    'EnhancedHasSlugModelAdminMixin',
    'EnhancedSluggedKaosModelAdminMixin',
)
