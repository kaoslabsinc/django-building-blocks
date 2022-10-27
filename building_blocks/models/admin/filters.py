from building_blocks.admin import QuerysetChoiceFilter


class ArchivableAdminFilter(QuerysetChoiceFilter):
    title = "Availability"
    parameter_name = 'availability'
    queryset_filters = ('available', 'archived')
