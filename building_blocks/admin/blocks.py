from django.contrib import admin

from .filters import ArchiveStatusFilter
from .mixins import EditReadonlyAdminMixin


class AdminBlock(admin.ModelAdmin):
    pass


class HasUUIDAdminBlock(AdminBlock):
    search_fields = ('uuid',)
    list_display = ('uuid',)
    list_display_shortcode = ('shortcode',)
    list_display_verbose = list_display + list_display_shortcode

    readonly_fields = ('uuid', 'shortcode',)
    fields = ('uuid',)
    fieldsets = (
        ("Identifiers", {'fields': fields}),
    )
    fieldsets_shortcode = (
        ("Identifiers", {'fields': ('shortcode',)}),
    )
    fieldsets_all = (
        ("Identifiers", {'fields': (*fields, 'shortcode',)}),
    )


class ArchivableAdminBlock(AdminBlock):
    list_display = ('archive_status',)
    list_filter = (ArchiveStatusFilter,)

    readonly_fields = ('archive_status', 'archived_at', 'is_active')
    fields = ('archive_status', 'archived_at',)
    fieldsets = (
        ("Management", {'fields': fields}),
    )


class PublishableAdminBlock(AdminBlock):
    list_display = ('publishing_stage',)
    list_filter = ('publishing_stage',)

    readonly_fields = ('publishing_stage', 'publishing_stage_changed_at',)
    fields = ('publishing_stage', 'publishing_stage_changed_at',)
    fieldsets = (
        ("Publishing", {'fields': fields}),
    )


class HasInitialsAdminBlock(AdminBlock):
    list_display = ('initials',)

    readonly_fields = ('initials',)
    fields = ('initials',)
    fieldsets = (
        ("Misc.", {'fields': fields}),
    )


class HasNameAdminBlock(AdminBlock):
    search_fields = ('name',)
    list_display = ('name',)
    fields = ('name',)


class HasEmailAdminBlock(AdminBlock):
    search_fields = ('email',)
    list_display = ('email',)
    fields = ('email',)


class HasDescriptionAdminBlock(AdminBlock):
    fields = ('description',)


class HasCoverPhotoAdminBlock(AdminBlock):
    fields = ('cover_photo',)
    fieldsets = (
        ("Media", {'fields': fields}),
    )


class HasIconAdminBlock(AdminBlock):
    fields = ('icon',)
    fieldsets = (
        ("Media", {'fields': fields}),
    )


class HasUserAdminBlock(EditReadonlyAdminMixin, AdminBlock):
    search_fields = ('user__username',)
    list_display = ('user',)

    edit_readonly_fields = ('user',)
    autocomplete_fields = ('user',)
    fields = ('user',)


class HasAutoSlugAdminBlock(EditReadonlyAdminMixin, AdminBlock):
    search_fields = ('slug',)
    list_display = ('slug',)
    readonly_fields = ('slug',)
    edit_readonly_fields = ('slug',)
    fields = ('slug',)
    fieldsets = (
        ("Identifiers", {'fields': fields}),
    )


class TimeStampedModelAdminBlock(admin.ModelAdmin):
    list_filter = ('created',)
    list_filter_extra = ('modified',)
    list_display = ('created',)
    list_display_extra = ('modified',)
    readonly_fields = ('created', 'modified')
    fields = ('created', 'modified')
    fieldsets = (
        ("Timestamps", {'fields': fields}),
    )


class HasAvatarAdminBlock(AdminBlock):
    fields = ('avatar',)
    fieldsets = (
        ("Media", {'fields': fields}),
    )
