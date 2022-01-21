from django.contrib import admin


class QuerysetChoiceFilter(admin.SimpleListFilter):
    default_value = 'all'
    queryset_filters = ()

    def lookups(self, request, model_admin):
        return [(filter_name, filter_name.replace('_', ' ').capitalize()) for filter_name in self.queryset_filters]

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
