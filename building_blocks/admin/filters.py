from django.contrib import admin

from building_blocks.models.admin.abstracts.filters import *

ArchivableFilter = ArchivableAdminFilter  # For compatibility # TODO: remove
PublishableFilter = PublishableAdminFilter  # For compatibility # TODO: remove


class QuerysetChoiceFilter(admin.SimpleListFilter):
    queryset_filters = ()

    def lookups(self, request, model_admin):
        lookups = []
        for filter_def in self.queryset_filters:
            if isinstance(filter_def, tuple):
                key, verbose_name = filter_def
            else:
                key, verbose_name = filter_def, filter_def.replace('_', ' ').capitalize()
            lookups.append((key, verbose_name))
        return lookups

    def queryset(self, request, queryset):
        value = self.value()
        if value in self.queryset_filters:
            return getattr(queryset, value)()
        return queryset


__all__ = [
    'QuerysetChoiceFilter',
    # TODO: remove
    'PublishableFilter',
    'ArchivableAdminFilter',
    'ArchivableFilter',
]
