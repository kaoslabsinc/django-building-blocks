from django.contrib import admin
from django.contrib.admin.options import BaseModelAdmin


class BaseArchivableAdmin(BaseModelAdmin):
    readonly_fields = ('is_archived', 'is_available')
    fields = ('is_available',)
    fieldsets = (
        ("Management", {'fields': fields}),
    )

    @admin.display(description="✔️", boolean=True, ordering='is_archived')
    def is_available(self, obj):
        return obj and obj.is_available

    @admin.display(boolean=True, ordering='is_archived')
    def is_archived(self, obj):
        return obj and obj.is_archived


__all__ = (
    'BaseArchivableAdmin',
)
