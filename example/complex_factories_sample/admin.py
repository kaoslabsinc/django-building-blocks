from django.contrib import admin

from building_blocks.admin.blocks import (
    HasUserAdminBlock, HasNameAdminBlock,
)
from complex_factories_sample.models import (
    HasUserExample, HasOptionalUserExample, HasOneToOneUserExample, HasOptionalOneToOneUserExample,
    HasAutoCodeGenerateFunctionExample,
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
class HasAutoCodeGenerateFunctionExampleAdmin(admin.ModelAdmin):
    search_fields = (
        *HasNameAdminBlock.search_fields,
    )
    list_display = (
        *HasNameAdminBlock.list_display,
        'code',
    )
    readonly_fields = (
        'code',
    )
    fields = (
        *HasNameAdminBlock.fields,
        'code'
    )
