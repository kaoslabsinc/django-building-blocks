from dj_kaos_utils.admin import AreYouSureActionsAdminMixin
from django.contrib import admin, messages
from django_object_actions import takes_instance_or_queryset

from building_blocks.models.enums import PublishStatus
from .archivable import ArchivableAdminBlock, BaseStatusArchivableMixinAdmin, ArchivableChangeActionsAdminMixin
from .filters import PublishableAdminFilter
from .status import HasStatusAdminBlock
from ..blocks import KaosModelAdminBlock, SluggedKaosModelAdminBlock
from ..utils import combine_admin_blocks_factory


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
    admin_fields = HasStatusAdminBlock.admin_fields + ArchivableAdminBlock.admin_fields
    extra_admin_fields = fields

    actions = (*ArchivableAdminBlock.actions, 'publish', 'unpublish')
    list_filter = (PublishableAdminFilter,)
    list_filter_extra = list_filter + HasStatusAdminBlock.list_filter


PublishableKaosModelAdminBlock = combine_admin_blocks_factory(
    PublishableAdminBlock,
    KaosModelAdminBlock
)

PublishableSluggedKaosModelAdminBlock = combine_admin_blocks_factory(
    PublishableAdminBlock,
    SluggedKaosModelAdminBlock
)


class BasePublishableMixinAdmin(BaseStatusArchivableMixinAdmin):
    readonly_fields = PublishableAdminBlock.readonly_fields

    @admin.display(boolean=True, ordering='status')
    def is_published(self, obj):
        return obj and obj.is_published

    @admin.display(boolean=True, ordering='status')
    def is_draft(self, obj):
        return obj and obj.is_draft


class BasicPublishableMixinAdmin(BasePublishableMixinAdmin, admin.ModelAdmin):
    actions = PublishableAdminBlock.actions

    list_display = PublishableAdminBlock.list_display
    list_filter = PublishableAdminBlock.list_filter

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


class PublishableMixinAdmin(
    AreYouSureActionsAdminMixin,
    ArchivableChangeActionsAdminMixin,
    BasicPublishableMixinAdmin
):
    change_actions = BasicPublishableMixinAdmin.actions
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


__all__ = (
    'PublishableAdminBlock',
    'PublishableKaosModelAdminBlock',
    'PublishableSluggedKaosModelAdminBlock',
    'BasePublishableMixinAdmin',
    'BasicPublishableMixinAdmin',
    'PublishableMixinAdmin',
)
