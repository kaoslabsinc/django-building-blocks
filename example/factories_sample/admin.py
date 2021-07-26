from django.contrib import admin

from building_blocks.admin.blocks import HasNameAdminBlock
from factories_sample.models import HasNameExample, HasOptionalNameExample


@admin.register(HasNameExample, HasOptionalNameExample)
class HasNameExampleAdmin(admin.ModelAdmin):
    search_fields = (
        *HasNameAdminBlock.search_fields,
    )
    list_display = (
        *HasNameAdminBlock.list_display,
    )
    fields = (
        *HasNameAdminBlock.fields,
    )

