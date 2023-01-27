from dj_kaos_utils.admin.utils import render_img, render_anchor
from django.contrib import admin, messages
from django.contrib.admin.options import BaseModelAdmin
from django.shortcuts import redirect
from django_object_actions import DjangoObjectActions, takes_instance_or_queryset

from building_blocks.consts.field_names import LINK_DISPLAY
from .models.interfaces import HasVisualizationInterface


class WithLinkDisplayAdminMixin:
    """
    Add a `link_display` admin display method to show a certain url as a link.
    """
    link_field = None
    link_content = "🔗 Link"

    list_display = (LINK_DISPLAY,)
    readonly_fields = (LINK_DISPLAY,)

    def get_link_url(self, obj):
        if self.link_field:
            return getattr(obj, self.link_field)

    def get_link_content(self, obj):
        if self.link_content is None:
            return self.get_link_url(obj)
        return self.link_content

    @admin.display(description="link")
    def link_display(self, obj):
        link_url = self.get_link_url(obj)
        if link_url:
            return render_anchor(link_url, self.get_link_content(obj))


class WithVisualizeAdminMixin(BaseModelAdmin):
    readonly_fields = (
        'visualize_display',
    )
    fieldsets = (
        ("Display", {'fields': ('visualize_display',)}),
    )

    @admin.display(description="visualize")
    def visualize_display(self, obj: HasVisualizationInterface):
        raise NotImplementedError


class WithSVGVisualizeAdminMixin(WithVisualizeAdminMixin):
    @admin.display(description="visualize")
    def visualize_display(self, obj: HasVisualizationInterface):
        if not obj:
            return
        return render_img(f"data:image/svg+xml;utf8,{obj.visualize()}", attrs={'style': "max-width: 100%;"})


class WithPNGVisualizeAdminMixin(WithVisualizeAdminMixin):
    @admin.display(description="visualize")
    def visualize_display(self, obj: HasVisualizationInterface):
        if not obj:
            return
        return render_img(f"data:image/png;base64,{obj.visualize()}", attrs={'style': "max-width: 100%;"})


class DuplicableAdminMixin(DjangoObjectActions):
    change_actions = ('duplicate',)

    @admin.action
    def duplicate(self, request, obj):
        new_obj = obj.duplicate()
        opts = new_obj._meta
        return redirect(f'admin:{opts.app_label}_{opts.model_name}_change', new_obj.id)


class SnapshotableAdminMixin(DjangoObjectActions):
    @admin.action
    def snapshot(self, request, obj):
        instance = obj.snapshot()
        opts = instance._meta
        return redirect(f'admin:{opts.app_label}_{opts.model_name}_change', instance.id)

    change_actions = ('snapshot',)


class HasImageAdminMixin(BaseModelAdmin):
    @admin.display(description="image")
    def image_display(self, obj):
        if not obj:
            return
        return render_anchor(obj.image.url, render_img(obj.image.url, attrs={'style': "max-width: 100%;"}))

    readonly_fields = ('image_display',)
    fieldsets = (
        ("Display", {'fields': ('image_display',)}),
    )


class HasGeneratableImageAdminMixin(DjangoObjectActions, HasImageAdminMixin):
    change_actions = ('generate_image',)
    actions = change_actions

    @takes_instance_or_queryset
    @admin.action
    def generate_image(self, request, queryset):
        for obj in queryset:
            obj.generate_image()
        messages.success(request, f"Generated {queryset.count()} images")


class HasTimeRangeAdmin(BaseModelAdmin):
    readonly_fields = (
        'time_range__start',
        'time_range__end',
    )
    fields = (
        '_time_range_dynamic',
        '_time_range_start',
        '_time_range_end',
    )


__all__ = (
    'WithLinkDisplayAdminMixin',
    'WithVisualizeAdminMixin',
    'WithSVGVisualizeAdminMixin',
    'WithPNGVisualizeAdminMixin',
    'DuplicableAdminMixin',
    'SnapshotableAdminMixin',
    'HasImageAdminMixin',
    'HasGeneratableImageAdminMixin',
    'HasTimeRangeAdmin',
)
