from django.contrib.admin.options import InlineModelAdmin


class AddInlineMixin(InlineModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.none()  # no existing records will appear


class ListInlineMixin(InlineModelAdmin):
    def has_add_permission(self, request, obj):
        return False


class ReadOnlyInlineMixin(ListInlineMixin):
    def has_change_permission(self, request, obj=None):
        return False
