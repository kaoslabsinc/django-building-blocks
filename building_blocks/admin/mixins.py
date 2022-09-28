from django.contrib.admin.options import BaseModelAdmin
from django_object_actions import BaseDjangoObjectActions


class PrepopulateSlugAdminMixin(BaseModelAdmin):
    """
    Makes the inheriting admin prepopulate the slug field from the field denoted by `slug_source`.
    Assumes by default, the slug field is ``model.slug``. If the field name is different, you can set it with
    `slug_field`.
    """
    slug_field = 'slug'
    slug_source = None

    def get_prepopulated_fields(self, request, obj=None):
        assert self.slug_source
        prepopulated_fields = super().get_prepopulated_fields(request, obj)
        if obj:  # editing an existing object
            return prepopulated_fields
        return {**prepopulated_fields, self.slug_field: (self.slug_source,)}


class DjangoObjectActionsPermissionsMixin(BaseDjangoObjectActions):
    """
    Built on DjangoObjectActions Admin, it checks if the user has change permissions on the object in order to show the
    change actions
    """

    def get_change_actions(self, request, object_id, form_url):
        obj = self.model.objects.get(pk=object_id)
        self.__obj = obj
        if not self.has_change_permission(request, obj):
            return ()
        else:
            return super(DjangoObjectActionsPermissionsMixin, self).get_change_actions(request, object_id, form_url)

    def _get_change_action_object(self):
        return self.__obj


class AreYouSureActionsAdminMixin(BaseDjangoObjectActions):
    are_you_sure_actions = ()
    are_you_sure_prompt_f = "Are you sure you want to {label} this object?"

    def __init__(self, *args, **kwargs):
        super(AreYouSureActionsAdminMixin, self).__init__(*args, **kwargs)
        for action in self.are_you_sure_actions:
            tool = getattr(self, action)
            label = getattr(tool, 'label', action).lower()
            are_you_sure_prompt = self.are_you_sure_prompt_f.format(tool=tool, label=label)
            tool.__dict__.setdefault('attrs', {})
            tool.__dict__['attrs'].setdefault('onclick', f"""return confirm("{are_you_sure_prompt}");""")


__all__ = [
    'PrepopulateSlugAdminMixin',
    'DjangoObjectActionsPermissionsMixin',
    'AreYouSureActionsAdminMixin',
]
