from django.contrib.admin.options import BaseModelAdmin


class CheckUserAdminMixin(BaseModelAdmin):
    """
    Limit access to objects who don't pass the check denoted by check_user() or has_see_all_permission().
    """

    def has_see_all_permission(self, request):
        raise NotImplementedError

    def check_user(self, request, obj):
        raise NotImplementedError

    def check_user_q(self, request):
        raise NotImplementedError

    def has_view_permission(self, request, obj=None):
        return super(CheckUserAdminMixin, self).has_view_permission(request, obj) and (
            obj is None or self.has_see_all_permission(request) or self.check_user(request, obj)
        )

    def has_change_permission(self, request, obj=None):
        return super(CheckUserAdminMixin, self).has_change_permission(request, obj) and (
            obj is None or self.has_see_all_permission(request) or self.check_user(request, obj)
        )

    def has_delete_permission(self, request, obj=None):
        return super(CheckUserAdminMixin, self).has_delete_permission(request, obj) and (
            obj is None or self.has_see_all_permission(request) or self.check_user(request, obj)
        )

    def get_queryset(self, request):
        qs = super(CheckUserAdminMixin, self).get_queryset(request)
        if self.has_see_all_permission(request):
            return qs
        return qs.filter(self.check_user_q(request))
