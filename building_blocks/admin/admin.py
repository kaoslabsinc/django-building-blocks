from django.contrib import admin
from django.contrib.auth import get_permission_codename
from django.utils.timezone import now
from django_object_actions import DjangoObjectActions, takes_instance_or_queryset

from ..models import Archivable, Publishable
from ..models.enums import PublishingStage


class ArchivableAdmin(DjangoObjectActions, admin.ModelAdmin):
    actions = ('archive', 'restore')
    change_actions = ('archive', 'restore')

    @admin.display(ordering='archived_at')
    def archive_status(self, obj: Archivable):
        return obj.archive_status.capitalize()

    @takes_instance_or_queryset
    def archive(self, request, queryset):
        queryset.update(archived_at=now())

    @takes_instance_or_queryset
    def restore(self, request, queryset):
        queryset.update(archived_at=None)

    def get_change_actions(self, request, object_id, form_url):
        change_actions = super().get_change_actions(request, object_id, form_url)
        change_actions = list(change_actions)
        obj: Archivable = self.model.objects.get(pk=object_id)
        if obj.is_active:
            change_actions.remove('restore')
        else:
            change_actions.remove('archive')

        return change_actions


class PublishableAdmin(DjangoObjectActions, admin.ModelAdmin):
    change_actions = ('publish', 'unpublish', 'archive', 'restore')

    def publish(self, request, obj: Publishable):
        obj.publish()
        obj.save()

    def unpublish(self, request, obj: Publishable):
        obj.unpublish()
        obj.save()

    def archive(self, request, obj: Publishable):
        obj.archive()
        obj.save()

    def restore(self, request, obj: Publishable):
        obj.restore()
        obj.save()

    def get_change_actions(self, request, object_id, form_url):
        change_actions = super().get_change_actions(request, object_id, form_url)
        change_actions = list(change_actions)
        obj: Publishable = self.model.objects.get(pk=object_id)

        if obj.publishing_stage != PublishingStage.archived:
            change_actions.remove('restore')
        if obj.publishing_stage != PublishingStage.published:
            change_actions.remove('unpublish')
        if obj.publishing_stage != PublishingStage.draft:
            change_actions.remove('publish')
        if obj.publishing_stage == PublishingStage.archived:
            change_actions.remove('archive')

        return change_actions


class HasUserAdmin(admin.ModelAdmin):
    default_see_all_perm_codename = 'see_all'

    def has_see_all_permission(self, request):
        opts = self.opts
        codename = get_permission_codename(self.default_see_all_perm_codename, opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))

    def _has_permission_helper(self, request, obj=None):
        if self.has_see_all_permission(request):
            return True
        return obj and obj.user == request.user

    def has_view_permission(self, request, obj=None):
        return (
            super(HasUserAdmin, self).has_view_permission(request, obj) and self._has_permission_helper(request, obj)
        )

    def has_change_permission(self, request, obj=None):
        return (
            super(HasUserAdmin, self).has_change_permission(request, obj) and self._has_permission_helper(request, obj)
        )

    def has_delete_permission(self, request, obj=None):
        return (
            super(HasUserAdmin, self).has_delete_permission(request, obj) and self._has_permission_helper(request, obj)
        )

    def get_queryset(self, request):
        qs = super(HasUserAdmin, self).get_queryset(request)
        if self.has_see_all_permission(request):
            return qs
        return qs.filter(user=request.user)
