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


class ArchivableAdminBlock(AdminBlock):
    list_display = ('archive_status',)
    list_filter = (ArchiveStatusFilter,)

    readonly_fields = ('archive_status', 'archived_at', 'is_active')
    fieldsets = (
        ("Management", {'fields': ('archive_status', 'archived_at',)}),
    )


class PublishableAdminBlock(AdminBlock):
    list_display = ('publishing_stage',)
    list_filter = ('publishing_stage',)

    readonly_fields = ('publishing_stage', 'publishing_stage_changed_at',)
    fieldsets = (
        ("Publishing", {'fields': ('publishing_stage', 'publishing_stage_changed_at',)}),
    )


class HasInitialsAdminBlock(AdminBlock):
    list_display = ('initials',)

    readonly_fields = ('initials',)
    fieldsets = (
        ("Misc.", {'fields': ('initials',)}),
    )


class HasNameAdminBlock(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    fields = ('name',)


class HasEmailAdminBlock(admin.ModelAdmin):
    search_fields = ('email',)
    list_display = ('email',)
    fields = ('email',)


class HasDescriptionAdminBlock(admin.ModelAdmin):
    fields = ('description',)


class HasCoverPhotoAdminBlock(admin.ModelAdmin):
    fieldsets = (
        ("Media", {'fields': ('cover_photo',)}),
    )


class HasIconAdminBlock(admin.ModelAdmin):
    fieldsets = (
        ("Media", {'fields': ('icon',)}),
    )


class HasUserAdminBlock(admin.ModelAdmin):
    search_fields = ('user__username',)
    list_display = ('user',)

    autocomplete_fields = ('user',)
