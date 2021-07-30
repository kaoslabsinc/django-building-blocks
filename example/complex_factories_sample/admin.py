from django.contrib import admin

from building_blocks.admin.admin import HasUserAdmin
from building_blocks.admin.blocks import (
    HasUserAdminBlock, HasNameAdminBlock, HasAutoSlugAdminBlock,
)
from building_blocks.admin.mixins import EditReadonlyAdminMixin
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
        *HasUserAdminBlock.search_fields,
    )
    list_display = (
        *HasUserAdminBlock.list_display,
    )
    autocomplete_fields = (
        *HasUserAdminBlock.autocomplete_fields,
    )


@admin.register(HasAutoCodeGenerateFunctionExample)
class HasAutoCodeGenerateFunctionExampleAdmin(
    EditReadonlyAdminMixin,
    admin.ModelAdmin
):
    search_fields = (
        *HasNameAdminBlock.search_fields,
    )
    list_display = (
        *HasNameAdminBlock.list_display,
        'code',
    )
    form = unrequire_form(HasAutoCodeGenerateFunctionExample, ('code',))
    edit_readonly_fields = (
        'code',
    )
    fields = (
        *HasNameAdminBlock.fields,
        'code'
    )


@admin.register(HasAutoSlugExample)
class HasAutoSlugExampleAdmin(admin.ModelAdmin):
    search_fields = (
        *HasNameAdminBlock.search_fields,
        *HasAutoSlugAdminBlock.search_fields,
    )
    list_display = (
        *HasNameAdminBlock.list_display,
        *HasAutoSlugAdminBlock.list_display,
    )
    readonly_fields = (
        *HasAutoSlugAdminBlock.autocomplete_fields,
    )
    fieldsets = (
        (None, {'fields': (*HasNameAdminBlock.fields,)}),
        *HasAutoSlugAdminBlock.fieldsets,
    )


@admin.register(HasUserLimitedAccess)
class HasUserLimitedAccessAdmin(
    HasUserAdmin,
    HasUserExampleAdmin
):
    pass
