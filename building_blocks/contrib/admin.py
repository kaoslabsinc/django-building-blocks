from django.contrib import admin

from building_blocks.admin import HasNameAdmin, HasAutoSlugAdmin
from building_blocks.admin.mixins import PrepopulateSlugAdminMixin


class NameSlugModelAdmin(PrepopulateSlugAdminMixin, admin.ModelAdmin):
    slug_source = 'name'

    search_fields = (
        *HasNameAdmin.search_fields,
        *HasAutoSlugAdmin.search_fields,
    )
    list_display = (
        *HasNameAdmin.list_display,
        *HasAutoSlugAdmin.list_display,
    )
    fieldsets = (
        (None, {'fields': HasNameAdmin.fields}),
        *HasAutoSlugAdmin.fieldsets,
    )
