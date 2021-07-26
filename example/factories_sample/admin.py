from django.contrib import admin

from building_blocks.admin.blocks import (
    HasNameAdminBlock,
    HasEmailAdminBlock,
    HasDescriptionAdminBlock,
)
from factories_sample.models import (
    HasNameExample, HasOptionalNameExample,
    HasEmailExample, HasOptionalEmailExample,
    HasDescriptionExample, HasRequiredDescriptionExample,
)


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


@admin.register(HasEmailExample, HasOptionalEmailExample)
class HasEmailExampleAdmin(admin.ModelAdmin):
    search_fields = (
        *HasEmailAdminBlock.search_fields,
    )
    list_display = (
        *HasEmailAdminBlock.list_display,
    )
    fields = (
        *HasEmailAdminBlock.fields,
    )


@admin.register(HasDescriptionExample, HasRequiredDescriptionExample)
class HasDescriptionExampleAdmin(admin.ModelAdmin):
    fields = (
        *HasDescriptionAdminBlock.fields,
    )

