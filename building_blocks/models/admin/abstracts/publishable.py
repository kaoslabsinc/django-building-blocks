from django.contrib import admin, messages
from django_object_actions import takes_instance_or_queryset, DjangoObjectActions

from building_blocks.admin import AreYouSureActionsAdminMixin, DjangoObjectActionsPermissionsMixin
from building_blocks.models.enums import PublishStatus
from .archivable import *
from .filters import PublishableAdminFilter
from .status import HasStatusAdminBlock
from ..blocks import FieldsetTitle


class PublishableAdminBlock(HasStatusAdminBlock):
    fields = (
        'is_published',
        'is_draft',
    )
    readonly_fields = (
        *ArchivableAdminBlock.readonly_fields,
        *HasStatusAdminBlock.readonly_fields,
        *fields
    )
    admin_fields = HasStatusAdminBlock.admin_fields + ArchivableAdminBlock.readonly_fields
    extra_admin_fields = fields
    the_admin_fieldset = (FieldsetTitle.admin, {'fields': admin_fields})
    the_admin_fieldset_extra = (FieldsetTitle.admin, {'fields': admin_fields + extra_admin_fields})
    actions = (*ArchivableAdminBlock.actions, 'publish', 'unpublish')
    list_filter = (PublishableAdminFilter,)
    list_filter_extra = list_filter + HasStatusAdminBlock.list_filter


class BasePublishableAdminMixin(BaseStatusArchivableAdminMixin):
    readonly_fields = PublishableAdminBlock.readonly_fields

    @admin.display(boolean=True, ordering='status')
    def is_published(self, obj):
        return obj and obj.is_published

    @admin.display(boolean=True, ordering='status')
    def is_draft(self, obj):
        return obj and obj.is_draft


class PublishableAdminMixin(BasePublishableAdminMixin, admin.ModelAdmin):
    actions = PublishableAdminBlock.actions

    @takes_instance_or_queryset
    @admin.action(permissions=['change'])
    def publish(self, request, queryset):
        count = queryset.set_published()
        messages.success(request, f"Published {count} objects")

    @takes_instance_or_queryset
    @admin.action(permissions=['change'])
    def unpublish(self, request, queryset):
        count = queryset.set_unpublished()
        messages.success(request, f"Unpublished {count} objects")


class EnhancedPublishableAdminMixin(
    AreYouSureActionsAdminMixin,
    DjangoObjectActionsPermissionsMixin,
    DjangoObjectActions,
    PublishableAdminMixin
):
    change_actions = PublishableAdminMixin.actions
    are_you_sure_actions = change_actions

    def get_change_actions(self, request, object_id, form_url):
        change_actions = super().get_change_actions(request, object_id, form_url)
        if change_actions:
            change_actions = list(change_actions)
            obj = self._get_change_action_object()
            if obj.status != PublishStatus.published:
                change_actions.remove('unpublish')
            if obj.status != PublishStatus.draft:
                change_actions.remove('publish')

        return change_actions
