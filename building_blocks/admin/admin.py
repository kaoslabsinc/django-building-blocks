from django.contrib import admin
from django.contrib.admin.options import BaseModelAdmin
from django_object_actions import takes_instance_or_queryset

from .filters import ArchiveStatusFilter, PublishingStatusFilter
from .mixins import DjangoObjectActionsPermissionsMixin, AreYouSureActionsAdminMixin, EditReadonlyAdminMixin
from ..models import Publishable
from ..models.enums import ArchiveStatus, PublishingStatus


class HasUUIDAdmin(admin.ModelAdmin):
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


class HasInitialsAdmin(admin.ModelAdmin):
    list_display = ('initials',)

    readonly_fields = ('initials',)
    fields = ('initials',)
    fieldsets = (
        ("Misc.", {'fields': fields}),
    )


class HasNameAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    fields = ('name',)


class HasEmailAdmin(admin.ModelAdmin):
    search_fields = ('email',)
    list_display = ('email',)
    fields = ('email',)


class HasDescriptionAdmin(admin.ModelAdmin):
    fields = ('description',)


class HasCoverPhotoAdmin(admin.ModelAdmin):
    fields = ('cover_photo',)
    fieldsets = (
        ("Media", {'fields': fields}),
    )


class HasIconAdmin(admin.ModelAdmin):
    fields = ('icon',)
    fieldsets = (
        ("Media", {'fields': fields}),
    )


class HasStatusAdmin(BaseModelAdmin):
    list_display = ('get_status_display',)
    readonly_fields = ('get_status_display',)
    fields = ('get_status_display',)

    @admin.display(ordering='-status')
    def self_status(self, obj):
        return obj._status


class ArchivableAdmin(
    HasStatusAdmin,
    AreYouSureActionsAdminMixin,
    DjangoObjectActionsPermissionsMixin,
    admin.ModelAdmin
):
    actions = ('archive', 'restore')
    change_actions = actions
    are_you_sure_actions = actions

    list_filter = (ArchiveStatusFilter,)

    readonly_fields = (*HasStatusAdmin.readonly_fields, 'is_active')
    fields = HasStatusAdmin.fields
    fieldsets = (
        ("Management", {'fields': fields}),
    )

    @takes_instance_or_queryset
    @admin.action(permissions=['change'])
    def archive(self, request, queryset):
        queryset.update(_status=ArchiveStatus.archived)

    @takes_instance_or_queryset
    @admin.action(permissions=['change'])
    def restore(self, request, queryset):
        queryset.update(_status=ArchiveStatus.active)

    def get_change_actions(self, request, object_id, form_url):
        change_actions = super().get_change_actions(request, object_id, form_url)
        if change_actions:
            change_actions = list(change_actions)
            if self._get_change_action_object().is_active:
                change_actions.remove('restore')
            else:
                change_actions.remove('archive')

        return change_actions


class PublishableAdmin(
    HasStatusAdmin,
    AreYouSureActionsAdminMixin,
    DjangoObjectActionsPermissionsMixin,
    admin.ModelAdmin
):
    change_actions = ('publish', 'unpublish', 'archive', 'restore')
    are_you_sure_actions = change_actions

    list_filter = (PublishingStatusFilter,)

    readonly_fields = (*ArchivableAdmin.readonly_fields, 'first_published_at',)
    fields = (*ArchivableAdmin.fields, 'first_published_at',)
    fieldsets = (
        ("Publishing", {'fields': fields}),
    )

    @admin.action(permissions=['change'])
    def publish(self, request, obj: Publishable):
        obj.publish()
        obj.save()

    @admin.action(permissions=['change'])
    def unpublish(self, request, obj: Publishable):
        obj.unpublish()
        obj.save()

    @admin.action(permissions=['change'])
    def archive(self, request, obj: Publishable):
        obj.archive()
        obj.save()

    @admin.action(permissions=['change'])
    def restore(self, request, obj: Publishable):
        obj.restore()
        obj.save()

    def get_change_actions(self, request, object_id, form_url):
        change_actions = super().get_change_actions(request, object_id, form_url)
        if change_actions:
            change_actions = list(change_actions)
            obj: Publishable = self._get_change_action_object()
            if obj.status != PublishingStatus.archived:
                change_actions.remove('restore')
            if obj.status != PublishingStatus.published:
                change_actions.remove('unpublish')
            if obj.status != PublishingStatus.draft:
                change_actions.remove('publish')
            if obj.status == PublishingStatus.archived:
                change_actions.remove('archive')

        return change_actions


class HasUserAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)
    list_display = ('user',)

    edit_readonly_fields = ('user',)
    autocomplete_fields = ('user',)
    fields = ('user',)


class HasAutoSlugAdmin(EditReadonlyAdminMixin, admin.ModelAdmin):
    search_fields = ('slug',)
    list_display = ('slug',)
    readonly_fields = ('slug',)
    edit_readonly_fields = ('slug',)
    fields = ('slug',)
    fieldsets = (
        ("Identifiers", {'fields': fields}),
    )


class TimeStampedModelAdmin(admin.ModelAdmin):
    list_filter = ('created',)
    list_filter_extra = ('modified',)
    list_display = ('created',)
    list_display_extra = ('modified',)
    readonly_fields = ('created', 'modified')
    fields = ('created', 'modified')
    fieldsets = (
        ("Timestamps", {'fields': fields}),
    )


class HasAvatarAdmin(admin.ModelAdmin):
    fields = ('avatar',)
    fieldsets = (
        ("Media", {'fields': fields}),
    )


class OrderableAdmin(admin.ModelAdmin):
    ordering = ('order',)
    list_display = ('order',)
    list_editable = ('order',)
    fields = ('order',)
    fieldsets = (
        ("View", {'fields': fields}),
    )


__all__ = [
    'HasUUIDAdmin',
    'HasInitialsAdmin',
    'HasNameAdmin',
    'HasEmailAdmin',
    'HasDescriptionAdmin',
    'HasCoverPhotoAdmin',
    'HasIconAdmin',
    'ArchivableAdmin',
    'PublishableAdmin',
    'HasUserAdmin',
    'HasAutoSlugAdmin',
    'TimeStampedModelAdmin',
    'HasAvatarAdmin',
    'OrderableAdmin',
]
