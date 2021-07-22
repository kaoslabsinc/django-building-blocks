from django.contrib import admin

from building_blocks.admin.admin import ArchivableAdmin
from building_blocks.admin.blocks import HasUUIDAdminBlock, ArchivableAdminBlock
from sample.models import HasUUIDExample, ArchivableHasUUID


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
class ArchivableHasUUIDExampleAdmin(
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
