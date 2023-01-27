from dj_kaos_utils.admin import QuerysetChoiceFilter


class ArchivableAdminFilter(QuerysetChoiceFilter):
    """
    Admin filter to filter archivable objects by their availability status
    """
    title = "Availability"
    parameter_name = 'availability'
    queryset_filters = ('available', 'archived')


class PublishableAdminFilter(ArchivableAdminFilter):
    """
    Admin filter to filter publishable objects by their publishing status
    """
    title = "by publish status"
    parameter_name = 'publish_status'
    queryset_filters = (*ArchivableAdminFilter.queryset_filters, 'published', 'draft')


__all__ = (
    'ArchivableAdminFilter',
    'PublishableAdminFilter',
)
