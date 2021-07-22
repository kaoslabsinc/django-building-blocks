from django.contrib import admin

from building_blocks.admin.blocks import HasUUIDAdminBlock
from sample.models import HasUUIDExample


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
