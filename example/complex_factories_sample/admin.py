from django.contrib import admin

from building_blocks.admin.blocks import (
    HasUserAdminBlock,
)
from complex_factories_sample.models import (
    HasUserExample, HasOptionalUserExample, HasOneToOneUserExample, HasOptionalOneToOneUserExample,
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
