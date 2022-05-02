from django.contrib import admin

from building_blocks.admin import HasNameAdmin, HasEmailAdmin, HasDescriptionAdmin, HasCoverPhotoAdmin, \
    HasIconAdmin, HasAvatarAdmin
from factories_sample.models import (
    HasNameExample, HasOptionalNameExample,
    HasEmailExample, HasOptionalEmailExample,
    HasDescriptionExample, HasRequiredDescriptionExample,
    HasCoverPhotoExample, HasRequiredCoverPhotoExample,
    HasIconExample, HasRequiredIconExample, HasAvatarExample,
)


@admin.register(HasNameExample, HasOptionalNameExample)
class HasNameExampleAdmin(admin.ModelAdmin):
    search_fields = (
        *HasNameAdmin.search_fields,
    )
    list_display = (
        *HasNameAdmin.list_display,
    )
    fields = (
        *HasNameAdmin.fields,
    )


@admin.register(HasEmailExample, HasOptionalEmailExample)
class HasEmailExampleAdmin(admin.ModelAdmin):
    search_fields = (
        *HasEmailAdmin.search_fields,
    )
    list_display = (
        *HasEmailAdmin.list_display,
    )
    fields = (
        *HasEmailAdmin.fields,
    )


@admin.register(HasDescriptionExample, HasRequiredDescriptionExample)
class HasDescriptionExampleAdmin(admin.ModelAdmin):
    fields = (
        *HasDescriptionAdmin.fields,
    )


@admin.register(HasCoverPhotoExample, HasRequiredCoverPhotoExample)
class HasCoverPhotoExampleAdmin(admin.ModelAdmin):
    fieldsets = (
        *HasCoverPhotoAdmin.fieldsets,
    )


@admin.register(HasIconExample, HasRequiredIconExample)
class HasIconExampleAdmin(admin.ModelAdmin):
    fieldsets = (
        *HasIconAdmin.fieldsets,
    )


@admin.register(HasAvatarExample)
class HasAvatarExampleAdmin(admin.ModelAdmin):
    fieldsets = (
        *HasAvatarAdmin.fieldsets,
    )
