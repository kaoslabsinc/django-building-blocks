from django.contrib import admin


class QuerysetChoiceFilter(admin.SimpleListFilter):
    default_value = 'all'
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
        value = self.value() or self.default_value
        if value in self.queryset_filters:
            return getattr(queryset, value)()
        return queryset


class ArchiveStatusFilter(QuerysetChoiceFilter):
    title = "Archive status"
    parameter_name = 'status'
    queryset_filters = ('active', 'archived')


class PublishingStatusFilter(QuerysetChoiceFilter):
    title = "Publishing status"
    parameter_name = 'status'
    queryset_filters = ('draft', 'published', 'archived')
