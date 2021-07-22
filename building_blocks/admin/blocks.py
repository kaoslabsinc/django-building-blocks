from django.contrib import admin

from .filters import ArchiveStatusFilter


class AdminBlock(admin.ModelAdmin):
    pass


class HasUUIDAdminBlock(AdminBlock):
    search_fields = ('uuid',)
    list_display = ('uuid',)
    list_display_shortcode = ('shortcode',)
    list_display_verbose = list_display + list_display_shortcode

    readonly_fields = ('uuid', 'shortcode',)
    fieldsets = (
        ("Identifiers", {'fields': ('uuid',)}),
    )
    fieldsets_shortcode = (
        ("Identifiers", {'fields': ('shortcode',)}),
    )


class ArchivableAdminBlock(admin.ModelAdmin):
    list_display = ('archive_status',)
    list_filter = (ArchiveStatusFilter,)

    readonly_fields = ('archive_status', 'archived_at', 'is_active')
    fieldsets = (
        ("Management", {'fields': ('archive_status', 'archived_at',)}),
    )
