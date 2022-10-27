from django.contrib import admin, messages
from django.contrib.admin.options import BaseModelAdmin
from django_object_actions import takes_instance_or_queryset, DjangoObjectActions

from building_blocks.admin import AreYouSureActionsAdminMixin, DjangoObjectActionsPermissionsMixin
from .blocks import BaseAdminBlock
from .filters import ArchivableAdminFilter


class ArchivableAdminBlock(BaseAdminBlock):
    admin_fields = ('is_available',)
    extra_admin_fields = ('is_archived',)
    the_admin_fieldset = ("Admin", {'fields': admin_fields})
    the_admin_fieldset_extra = ("Admin", {'fields': admin_fields + extra_admin_fields})

    actions = ('archive', 'restore')
    list_display = admin_fields
    extra_list_display = extra_admin_fields


class BaseArchivableAdmin(BaseModelAdmin):
    readonly_fields = (
        *ArchivableAdminBlock.admin_fields,
        *ArchivableAdminBlock.extra_admin_fields,
    )

    @admin.display(description="✔️", boolean=True, ordering='is_archived')
    def is_available(self, obj):
        return obj and obj.is_available

    @admin.display(boolean=True, ordering='is_archived')
    def is_archived(self, obj):
        return obj and obj.is_archived


class ArchivableAdmin(
    BaseArchivableAdmin,
    admin.ModelAdmin
):
    actions = ArchivableAdminBlock.actions

    list_filter = (ArchivableAdminFilter,)
    list_display = ('is_available',)

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


class EnhancedArchivableAdmin(
    AreYouSureActionsAdminMixin,
    DjangoObjectActionsPermissionsMixin,
    DjangoObjectActions,
    ArchivableAdmin
):
    change_actions = ArchivableAdmin.actions
    are_you_sure_actions = change_actions

    def get_change_actions(self, request, object_id, form_url):
        change_actions = super().get_change_actions(request, object_id, form_url)
        if change_actions:
            change_actions = list(change_actions)
            if self._get_change_action_object().is_available:
                change_actions.remove('restore')
            else:
                change_actions.remove('archive')

        return change_actions


__all__ = (
    'ArchivableAdminBlock',
    'BaseArchivableAdmin',
    'EnhancedArchivableAdmin',
)
