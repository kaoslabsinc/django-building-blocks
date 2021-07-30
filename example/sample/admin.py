from django.contrib import admin

from building_blocks.admin.admin import ArchivableAdmin, PublishableAdmin
from building_blocks.admin.blocks import HasUUIDAdminBlock, ArchivableAdminBlock, PublishableAdminBlock, \
    HasInitialsAdminBlock, TimeStampedModelAdminBlock
from building_blocks.admin.inlines import AddInlineMixin, ListInlineMixin
from building_blocks.admin.utils import json_field_pp, render_anchor, render_img
from .models import HasUUIDExample, ArchivableHasUUID, PublishableHasUUID, HasInitialsExample, HasAutoFieldsExample, \
    TimeStampedExample, AdminUtilsExample, ContainerItem, Container


@admin.register(HasUUIDExample)
class HasUUIDExampleAdmin(admin.ModelAdmin):
    search_fields = (
        *HasUUIDAdminBlock.search_fields,
    )
    list_display = (
        *HasUUIDAdminBlock.list_display,
    )

    readonly_fields = (
        *HasUUIDAdminBlock.readonly_fields,
    )
    fieldsets = (
        *HasUUIDAdminBlock.fieldsets,
    )


@admin.register(ArchivableHasUUID)
class ArchivableHasUUIDAdmin(
    ArchivableAdmin,
    admin.ModelAdmin
):
    search_fields = (
        *HasUUIDAdminBlock.search_fields,
    )
    list_display = (
        *HasUUIDAdminBlock.list_display,
        *ArchivableAdminBlock.list_display,
    )
    list_filter = (
        *ArchivableAdminBlock.list_filter,
    )

    readonly_fields = (
        *HasUUIDAdminBlock.readonly_fields,
        *ArchivableAdminBlock.readonly_fields,
    )
    fieldsets = (
        *HasUUIDAdminBlock.fieldsets,
        *ArchivableAdminBlock.fieldsets,
    )


@admin.register(PublishableHasUUID)
class PublishableHasUUIDAdmin(
    PublishableAdmin,
    admin.ModelAdmin
):
    search_fields = (
        *HasUUIDAdminBlock.search_fields,
    )
    list_display = (
        *HasUUIDAdminBlock.list_display,
        *PublishableAdminBlock.list_display,
    )
    list_filter = (
        *PublishableAdminBlock.list_filter,
    )

    readonly_fields = (
        *HasUUIDAdminBlock.readonly_fields,
        *PublishableAdminBlock.readonly_fields,
    )
    fieldsets = (
        *HasUUIDAdminBlock.fieldsets,
        *PublishableAdminBlock.fieldsets,
    )


@admin.register(HasInitialsExample)
class HasInitialsExampleAdmin(
    admin.ModelAdmin
):
    list_display = (
        'full_name',
        *HasInitialsAdminBlock.list_display
    )

    readonly_fields = HasInitialsAdminBlock.readonly_fields
    fieldsets = (
        (None, {'fields': ('full_name',)}),
        *HasInitialsAdminBlock.fieldsets,
    )


@admin.register(HasAutoFieldsExample)
class HasAutoFieldsExampleAdmin(
    admin.ModelAdmin
):
    readonly_fields = ('name_upper',)


@admin.register(TimeStampedExample)
class TimeStampedExampleAdmin(
    admin.ModelAdmin
):
    list_filter = (
        *TimeStampedModelAdminBlock.list_filter, *TimeStampedModelAdminBlock.list_filter_extra
    )
    list_display = (
        *TimeStampedModelAdminBlock.list_display, *TimeStampedModelAdminBlock.list_display_extra
    )
    readonly_fields = (*TimeStampedModelAdminBlock.readonly_fields,)
    fieldsets = (*TimeStampedModelAdminBlock.fieldsets,)


@admin.register(AdminUtilsExample)
class AdminUtilsExampleAdmin(
    admin.ModelAdmin
):
    readonly_fields = ('json_pp', 'url_anchor', 'img')

    @admin.display
    def json_pp(self, obj: AdminUtilsExample):
        return json_field_pp(obj.json)

    @admin.display
    def url_anchor(self, obj: AdminUtilsExample):
        return render_anchor(obj.url, "Click me!")

    @admin.display
    def img(self, obj: AdminUtilsExample):
        return render_img(obj.image_url)


class ContainerItemInline(admin.TabularInline):
    model = ContainerItem
    extra = 0


class ContainerItemAddInline(AddInlineMixin, ContainerItemInline):
    pass


class ContainerItemListInline(ListInlineMixin, ContainerItemInline):
    readonly_fields = ('name',)
    fields = ('name', 'email')


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    inlines = (ContainerItemListInline, ContainerItemAddInline)
