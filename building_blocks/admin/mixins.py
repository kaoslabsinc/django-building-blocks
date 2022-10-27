from dj_kaos_utils.admin.utils import render_anchor
from django.contrib import admin


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


__all__ = (
    'WithLinkDisplayAdminMixin',
)
