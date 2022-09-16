from django.contrib.admin.options import BaseModelAdmin


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
