from django.contrib import admin

from building_blocks.admin.admin import HasUserAdmin, HasAutoSlugAdmin, HasNameAdmin
from building_blocks.admin.mixins import EditReadonlyAdminMixin, PrepopulateSlugAdminMixin
from building_blocks.forms import unrequire_form
from complex_factories_sample.models import (
    HasUserExample, HasOptionalUserExample, HasOneToOneUserExample, HasOptionalOneToOneUserExample,
    HasAutoCodeGenerateFunctionExample,
    HasAutoSlugExample,
    HasUserLimitedAccess,
)


@admin.register(HasUserExample, HasOptionalUserExample, HasOneToOneUserExample, HasOptionalOneToOneUserExample)
class HasUserExampleAdmin(admin.ModelAdmin):
    search_fields = (
        *HasUserAdmin.search_fields,
    )
    list_display = (
        *HasUserAdmin.list_display,
    )
    autocomplete_fields = (
        *HasUserAdmin.autocomplete_fields,
    )


@admin.register(HasAutoCodeGenerateFunctionExample)
class HasAutoCodeGenerateFunctionExampleAdmin(
    EditReadonlyAdminMixin,
    admin.ModelAdmin
):
    search_fields = (
        *HasNameAdmin.search_fields,
    )
    list_display = (
        *HasNameAdmin.list_display,
        'code',
    )
    form = unrequire_form(HasAutoCodeGenerateFunctionExample, ('code',))
    edit_readonly_fields = (
        'code',
    )
    fields = (
        *HasNameAdmin.fields,
        'code'
    )


@admin.register(HasAutoSlugExample)
class HasAutoSlugExampleAdmin(
    PrepopulateSlugAdminMixin,
    admin.ModelAdmin
):
    slug_source = 'name'
    form = unrequire_form(HasAutoSlugExample, ('slug',))

    search_fields = (
        *HasNameAdmin.search_fields,
        *HasAutoSlugAdmin.search_fields,
    )
    list_display = (
        *HasNameAdmin.list_display,
        *HasAutoSlugAdmin.list_display,
    )
    fieldsets = (
        (None, {'fields': (*HasNameAdmin.fields,)}),
        *HasAutoSlugAdmin.fieldsets,
    )


@admin.register(HasUserLimitedAccess)
class HasUserLimitedAccessAdmin(
    HasUserAdmin,
    HasUserExampleAdmin
):
    pass
