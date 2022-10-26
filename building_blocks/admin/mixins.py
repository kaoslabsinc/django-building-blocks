from dj_kaos_utils.admin.utils import render_anchor
from django.contrib import admin
from django.contrib.admin.options import BaseModelAdmin
from django.shortcuts import get_object_or_404
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
        obj = get_object_or_404(self.model, pk=object_id)
        self.__obj = obj
        if not self.has_change_permission(request, obj):
            return ()
        else:
            return super(DjangoObjectActionsPermissionsMixin, self).get_change_actions(request, object_id, form_url)

    def _get_change_action_object(self):
        return self.__obj


class AreYouSureActionsAdminMixin(BaseDjangoObjectActions):
    """
    Add a confirmation prompt to the certain object actions defined in `are_you_sure_actions`.
    """
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


class ExcludeFromNonSuperusersMixin(BaseModelAdmin):
    """
    Admin mixin to make some fields hidden to non-superusers. Define such fields using `.exclude_from_non_superusers`,
    or dynamically by overriding `.get_exclude_from_non_superusers()`.
    """
    exclude_from_non_superusers = ()

    def get_exclude_from_non_superusers(self, request, obj=None):
        return self.exclude_from_non_superusers

    def get_exclude(self, request, obj=None):
        exclude = super(ExcludeFromNonSuperusersMixin, self).get_exclude(request, obj) or ()
        if request.user.is_superuser:
            return exclude
        return (
            *exclude,
            *self.get_exclude_from_non_superusers(request, obj),
        )


class ExcludeFromFieldsetsMixin(BaseModelAdmin):
    """
    Admin mixin to make sure fields that are in `exclude` are removed from the `fieldsets` definition.
    By default, without this mixin, if a field defined in `fieldsets` is in `exclude`, Django throws an
    error complaining about a missing value for the field.
    """

    def get_fieldsets(self, request, obj=None):
        exclude = self.get_exclude(request, obj)
        fieldsets = super().get_fieldsets(request, obj) or ()
        return [
            (fieldset_name,
             {
                 **fieldset_dict,
                 'fields': [field for field in fieldset_dict['fields'] if field not in exclude]
             })
            for fieldset_name, fieldset_dict in fieldsets
        ]


class WithLinkDisplayAdminMixin:
    """
    Add a `link_display` admin display method to show a certain url as a link.
    """
    link_field = None
    link_content = "🔗 Link"

    list_display = ('link_display',)
    readonly_fields = ('link_display',)
    fields = ('link_display',)

    def get_link_url(self, obj):
        if self.link_field:
            return getattr(obj, self.link_field)

    def get_link_content(self, obj):
        if self.link_content is None:
            return self.get_link_url(obj)
        return self.link_content

    @admin.display(description="link")
    def link_display(self, obj):
        if link_url := self.get_link_url(obj):
            return render_anchor(link_url, self.get_link_content(obj))


__all__ = [
    'PrepopulateSlugAdminMixin',
    'DjangoObjectActionsPermissionsMixin',
    'AreYouSureActionsAdminMixin',
    'ExcludeFromNonSuperusersMixin',
    'ExcludeFromFieldsetsMixin',
    'WithLinkDisplayAdminMixin',
]
