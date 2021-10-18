from django.contrib import admin
from django.db.models import Q
from django.utils.timezone import now
from django_object_actions import takes_instance_or_queryset

from .mixins import CheckUserAdminMixin, DjangoObjectActionsPermissionsMixin, AreYouSureActionsAdminMixin
from ..models import Archivable, Publishable
from ..models.enums import PublishingStage


class ArchivableAdmin(
    AreYouSureActionsAdminMixin,
    DjangoObjectActionsPermissionsMixin,
    admin.ModelAdmin
):
    actions = ('archive', 'restore')
    change_actions = ('archive', 'restore')
    are_you_sure_actions = ('archive', 'restore')

    @admin.display(ordering='archived_at')
    def archive_status(self, obj: Archivable):
        return obj.archive_status.capitalize()

    @takes_instance_or_queryset
    @admin.action(permissions=['change'])
    def archive(self, request, queryset):
        queryset.update(archived_at=now())

    @takes_instance_or_queryset
    @admin.action(permissions=['change'])
    def restore(self, request, queryset):
        queryset.update(archived_at=None)

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
    AreYouSureActionsAdminMixin,
    DjangoObjectActionsPermissionsMixin,
    admin.ModelAdmin
):
    change_actions = ('publish', 'unpublish', 'archive', 'restore')
    are_you_sure_actions = ('publish', 'unpublish', 'archive', 'restore')

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
            if obj.publishing_stage != PublishingStage.archived:
                change_actions.remove('restore')
            if obj.publishing_stage != PublishingStage.published:
                change_actions.remove('unpublish')
            if obj.publishing_stage != PublishingStage.draft:
                change_actions.remove('publish')
            if obj.publishing_stage == PublishingStage.archived:
                change_actions.remove('archive')

        return change_actions


class HasUserAdmin(CheckUserAdminMixin, admin.ModelAdmin):
    """
    Limit access to objects who aren't 'owned' by the user (obj.user != request.user).
    The user needs to be either the owner or have the `see_all` permission on the model.
    """

    def check_user_q(self, request):
        return Q(user=request.user)
