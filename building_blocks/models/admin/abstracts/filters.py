from building_blocks.admin import QuerysetChoiceFilter


class ArchivableAdminFilter(QuerysetChoiceFilter):
    title = "Availability"
    parameter_name = 'availability'
    queryset_filters = ('available', 'archived')


class PublishableAdminFilter(ArchivableAdminFilter):
    title = "by publish status"
    parameter_name = 'publish_status'
    queryset_filters = (*ArchivableAdminFilter.queryset_filters, 'published', 'draft')


__all__ = (
    'ArchivableAdminFilter',
    'PublishableAdminFilter',
)
