from django.contrib import admin


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


class ArchivableFilter(QuerysetChoiceFilter):
    title = "Availability"
    parameter_name = 'availability'
    queryset_filters = ('available', 'archived')


__all__ = [
    'QuerysetChoiceFilter',
    'ArchivableFilter',
]
