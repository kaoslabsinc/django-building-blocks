from django.contrib.admin.options import BaseModelAdmin
from django_object_actions import DjangoObjectActions


class EditReadonlyAdminMixin(BaseModelAdmin):
    """
    Fields defined in edit_readonly_fields are editable upon creation, but after that they become readonly
    """
    edit_readonly_fields = ()

    def get_edit_readonly_fields(self, request, obj=None):
        return self.edit_readonly_fields

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:  # editing an existing object
            return self.get_edit_readonly_fields(request, obj) + readonly_fields
        return readonly_fields


class PrepopulateSlugAdminMixin(EditReadonlyAdminMixin):
    slug_source = None

    def get_prepopulated_fields(self, request, obj=None):
        assert self.slug_source
        prepopulated_fields = super().get_prepopulated_fields(request, obj)
        if obj:  # editing an existing object
            return prepopulated_fields
        return {**prepopulated_fields, 'slug': (self.slug_source,)}


class DjangoObjectActionsPermissionsMixin(DjangoObjectActions):
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


class AreYouSureActionsAdminMixin(DjangoObjectActions):
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
