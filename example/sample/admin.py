from django.contrib import admin

from building_blocks.admin.admin import ArchivableAdmin, PublishableAdmin
from building_blocks.admin.blocks import HasUUIDAdminBlock, ArchivableAdminBlock, PublishableAdminBlock, \
    HasInitialsAdminBlock
from .models import HasUUIDExample, ArchivableHasUUID, PublishableHasUUID, HasInitialsExample


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
