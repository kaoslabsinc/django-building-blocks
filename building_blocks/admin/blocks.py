from django.contrib import admin


class HasUUIDAdminBlock(admin.ModelAdmin):
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
