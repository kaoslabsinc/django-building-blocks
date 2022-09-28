from django.contrib import admin, messages
from django_object_actions import takes_instance_or_queryset, DjangoObjectActions

from .mixins import AreYouSureActionsAdminMixin, DjangoObjectActionsPermissionsMixin


class ArchivableAdmin(
    AreYouSureActionsAdminMixin,
    DjangoObjectActionsPermissionsMixin,
    DjangoObjectActions,
    admin.ModelAdmin
):
    actions = ('archive', 'restore')
    change_actions = actions
    are_you_sure_actions = actions

    list_filter = ('is_archived',)
    list_display = ('is_available',)

    readonly_fields = ('is_archived', 'is_available')
    fields = ('is_available',)
    fieldsets = (
        ("Management", {'fields': fields}),
    )

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

    def get_change_actions(self, request, object_id, form_url):
        change_actions = super().get_change_actions(request, object_id, form_url)
        if change_actions:
            change_actions = list(change_actions)
            if self._get_change_action_object().is_available:
                change_actions.remove('restore')
            else:
                change_actions.remove('archive')

        return change_actions

    @admin.display(boolean=True)
    def is_available(self, obj):
        return obj and obj.is_available


__all__ = [
    'ArchivableAdmin',
]
