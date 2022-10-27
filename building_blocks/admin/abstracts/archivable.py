from dj_kaos_utils.admin import AreYouSureActionsAdminMixin, DjangoObjectActionsPermissionsMixin
from django.contrib import admin, messages
from django.contrib.admin.options import BaseModelAdmin
from django_object_actions import takes_instance_or_queryset, DjangoObjectActions

from .filters import ArchivableAdminFilter
from ..blocks import FieldsetTitle, BaseAdminBlock, KaosModelAdminBlock, SluggedKaosModelAdminBlock


class ArchivableAdminBlock(BaseAdminBlock):
    admin_fields = ('is_available',)
    extra_admin_fields = ('is_archived',)
    the_admin_fieldset = (FieldsetTitle.admin, {'fields': admin_fields})
    the_admin_fieldset_extra = (FieldsetTitle.admin, {'fields': admin_fields + extra_admin_fields})

    actions = ('archive', 'restore')
    list_display = admin_fields
    list_filter = (ArchivableAdminFilter,)
    extra_list_display = extra_admin_fields
    readonly_fields = admin_fields + extra_admin_fields


class BaseArchivableMixinAdmin(BaseModelAdmin):
    readonly_fields = ArchivableAdminBlock.readonly_fields

    @admin.display(description="✔️", boolean=True, ordering='is_archived')
    def is_available(self, obj):
        return obj and obj.is_available

    @admin.display(boolean=True, ordering='is_archived')
    def is_archived(self, obj):
        return obj and obj.is_archived

    @takes_instance_or_queryset
    @admin.action(permissions=['change'])
    def archive(self, request, queryset):
        count = queryset.set_archived()
        messages.success(request, f"Archived {count} objects")

    @takes_instance_or_queryset
    @admin.action(permissions=['change'])
    def restore(self, request, queryset):
        count = queryset.set_restored()
        messages.success(request, f"Restored {count} objects")


class BaseStatusArchivableMixinAdmin(BaseArchivableMixinAdmin):
    readonly_fields = ArchivableAdminBlock.readonly_fields

    @admin.display(description="✔️", boolean=True, ordering='status')
    def is_available(self, obj):
        return super().is_available(obj)

    @admin.display(boolean=True, ordering='status')
    def is_archived(self, obj):
        return super().is_archived(obj)


class BasicArchivableMixinAdmin(
    BaseArchivableMixinAdmin,
    admin.ModelAdmin
):
    actions = ArchivableAdminBlock.actions

    list_display = ArchivableAdminBlock.list_display
    list_filter = ArchivableAdminBlock.list_filter


class ArchivableChangeActionsAdminMixin(
    DjangoObjectActionsPermissionsMixin,
    DjangoObjectActions
):
    def get_change_actions(self, request, object_id, form_url):
        change_actions = super().get_change_actions(request, object_id, form_url)
        if change_actions:
            change_actions = list(change_actions)
            if self._get_change_action_object().is_available:
                change_actions.remove('restore')
            else:
                change_actions.remove('archive')

        return change_actions


class ArchivableMixinAdmin(
    AreYouSureActionsAdminMixin,
    ArchivableChangeActionsAdminMixin,
    BasicArchivableMixinAdmin
):
    change_actions = BasicArchivableMixinAdmin.actions
    are_you_sure_actions = change_actions


class ArchivableKaosModelAdminBlock(ArchivableAdminBlock, KaosModelAdminBlock):
    admin_fields = (
        *ArchivableAdminBlock.admin_fields,
        *KaosModelAdminBlock.admin_fields,
    )
    extra_admin_fields = (
        *ArchivableAdminBlock.extra_admin_fields,
        *KaosModelAdminBlock.extra_admin_fields,
    )
    the_admin_fieldset = (FieldsetTitle.admin, {'fields': admin_fields})
    the_admin_fieldset_extra = (FieldsetTitle.admin, {'fields': admin_fields + extra_admin_fields})


class ArchivableSluggedKaosModelAdminBlock(ArchivableAdminBlock, SluggedKaosModelAdminBlock):
    admin_fields = (
        *ArchivableAdminBlock.admin_fields,
        *SluggedKaosModelAdminBlock.admin_fields,
    )
    extra_admin_fields = (
        *ArchivableAdminBlock.extra_admin_fields,
        *SluggedKaosModelAdminBlock.extra_admin_fields,
    )
    the_admin_fieldset = (FieldsetTitle.admin, {'fields': admin_fields})
    the_admin_fieldset_extra = (FieldsetTitle.admin, {'fields': admin_fields + extra_admin_fields})


__all__ = (
    'ArchivableAdminBlock',
    'BaseArchivableMixinAdmin',
    'BaseStatusArchivableMixinAdmin',
    'BasicArchivableMixinAdmin',
    'ArchivableChangeActionsAdminMixin',
    'ArchivableMixinAdmin',
    'ArchivableKaosModelAdminBlock',
)
