from dj_kaos_utils.admin.utils import render_img, render_anchor
from django.contrib import admin, messages
from django.contrib.admin.options import BaseModelAdmin
from django.shortcuts import redirect
from django_object_actions import DjangoObjectActions, takes_instance_or_queryset

from .models.mixins import HasVisualizationMixin


class WithVisualizeAdminMixin(BaseModelAdmin):
    readonly_fields = (
        'visualize_display',
    )
    fieldsets = (
        ("Display", {'fields': ('visualize_display',)}),
    )

    @admin.display(description="visualize")
    def visualize_display(self, obj: HasVisualizationMixin):
        raise NotImplementedError


class WithSVGVisualizeAdminMixin(WithVisualizeAdminMixin):
    @admin.display(description="visualize")
    def visualize_display(self, obj: HasVisualizationMixin):
        if not obj:
            return
        return render_img(f"data:image/svg+xml;utf8,{obj.visualize()}", attrs={'style': "max-width: 100%;"})


class WithPNGVisualizeAdminMixin(WithVisualizeAdminMixin):
    @admin.display(description="visualize")
    def visualize_display(self, obj: HasVisualizationMixin):
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
    'WithVisualizeAdminMixin',
    'WithSVGVisualizeAdminMixin',
    'WithPNGVisualizeAdminMixin',
    'DuplicableAdminMixin',
    'SnapshotableAdminMixin',
    'HasImageAdminMixin',
    'HasGeneratableImageAdminMixin',
    'HasTimeRangeAdmin',
)
