from django.contrib import admin
from django.utils.timezone import now
from django_object_actions import DjangoObjectActions, takes_instance_or_queryset

from ..abstracts import Archivable


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
