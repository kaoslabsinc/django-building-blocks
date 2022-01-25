from django.contrib import admin

from building_blocks.admin.admin import ArchivableAdmin, PublishableAdmin, HasUUIDAdmin, HasInitialsAdmin, \
    TimeStampedModelAdmin, OrderableAdmin, HasNameAdmin
from building_blocks.admin.inlines import AddInlineMixin, ListInlineMixin
from building_blocks.admin.utils import json_field_pp, render_anchor, render_img
from .models import HasUUIDExample, ArchivableHasUUID, PublishableHasUUID, HasInitialsExample, HasAutoFieldsExample, \
    TimeStampedExample, AdminUtilsExample, ContainerItem, Container, LowerCaseCharFieldExample, OrderedStuff


@admin.register(HasUUIDExample)
class HasUUIDExampleAdmin(admin.ModelAdmin):
    search_fields = (
        *HasUUIDAdmin.search_fields,
    )
    list_display = (
        *HasUUIDAdmin.list_display,
    )

    readonly_fields = (
        *HasUUIDAdmin.readonly_fields,
    )
    fieldsets = (
        *HasUUIDAdmin.fieldsets,
    )


@admin.register(ArchivableHasUUID)
class ArchivableHasUUIDAdmin(
    ArchivableAdmin,
    admin.ModelAdmin
):
    search_fields = (
        *HasUUIDAdmin.search_fields,
    )
    list_display = (
        *HasUUIDAdmin.list_display,
        *ArchivableAdmin.list_display,
    )
    list_filter = (
        *ArchivableAdmin.list_filter,
    )

    readonly_fields = (
        *HasUUIDAdmin.readonly_fields,
        *ArchivableAdmin.readonly_fields,
    )
    fieldsets = (
        *HasUUIDAdmin.fieldsets,
        *ArchivableAdmin.fieldsets,
    )


@admin.register(PublishableHasUUID)
class PublishableHasUUIDAdmin(
    PublishableAdmin,
    admin.ModelAdmin
):
    search_fields = (
        *HasUUIDAdmin.search_fields,
    )
    list_display = (
        *HasUUIDAdmin.list_display,
        *PublishableAdmin.list_display,
    )
    list_filter = (
        *PublishableAdmin.list_filter,
    )

    readonly_fields = (
        *HasUUIDAdmin.readonly_fields,
        *PublishableAdmin.readonly_fields,
    )
    fieldsets = (
        *HasUUIDAdmin.fieldsets,
        *PublishableAdmin.fieldsets,
    )


@admin.register(HasInitialsExample)
class HasInitialsExampleAdmin(
    admin.ModelAdmin
):
    list_display = (
        'full_name',
        *HasInitialsAdmin.list_display
    )

    readonly_fields = HasInitialsAdmin.readonly_fields
    fieldsets = (
        (None, {'fields': ('full_name',)}),
        *HasInitialsAdmin.fieldsets,
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
        *TimeStampedModelAdmin.list_filter, *TimeStampedModelAdmin.list_filter_extra
    )
    list_display = (
        *TimeStampedModelAdmin.list_display, *TimeStampedModelAdmin.list_display_extra
    )
    readonly_fields = (*TimeStampedModelAdmin.readonly_fields,)
    fieldsets = (*TimeStampedModelAdmin.fieldsets,)


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


admin.site.register(LowerCaseCharFieldExample)


@admin.register(OrderedStuff)
class OrderedStuffAdmin(admin.ModelAdmin):
    ordering = OrderableAdmin.ordering
    list_display = (*HasNameAdmin.list_display, *OrderableAdmin.list_display)
    list_editable = OrderableAdmin.list_editable
    fieldsets = (
        (None, {'fields': HasNameAdmin.fields}),
        *OrderableAdmin.fieldsets,
    )
