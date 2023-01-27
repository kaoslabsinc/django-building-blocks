"""
BaseModelAdmins for Kaos Models
"""

from django.contrib.admin.options import BaseModelAdmin

from .blocks import *
from .mixins import EnhancedSluggedKaosModelAdminMixin


class BaseKaosModelAdmin(BaseModelAdmin):
    """
    Base model admin for `KaosModel`

    :param ordering: None
    :param exclude: None
    :param fields: None
    :param autocomplete_fields: ()
    :param readonly_fields: ('uuid', 'created', 'modified')
    :param fieldsets: ((None, {'fields': (('name',),)}), ('Admin', {'fields': ('uuid', 'created')}))
    """
    readonly_fields = KaosModelAdminBlock.readonly_fields
    fieldsets = (
        (None, {'fields': (KaosModelAdminBlock.base_fields,)}),
        KaosModelAdminBlock.the_admin_fieldset,
    )


class BaseKaosModelAdminExtra(BaseKaosModelAdmin):
    """
    `BaseKaosModelAdmin` with extra admin fields (modified)

    :param fieldsets: ((None, {'fields': (('name',),)}), ('Admin', {'fields': ('uuid', 'created', 'modified')}))
    """
    fieldsets = (
        *BaseKaosModelAdmin.fieldsets[:-1],
        KaosModelAdminBlock.the_admin_fieldset_extra,
    )


class BaseBasicSluggedKaosModelAdmin(BaseKaosModelAdmin):
    """
    Basic Base model admin for `SluggedKaosModel`.

    This basic admin lacks fancy features for slug like prepopulate, edit readonly or being unrequired.

    Mixing this and `EnhancedSluggedKaosModelAdminMixin` results in `BaseSluggedKaosModelAdmin`.

    :param ordering: None
    :param exclude: None
    :param fields: None
    :param autocomplete_fields: ()
    :param readonly_fields: ('uuid', 'created', 'modified')
    :param fieldsets: ((None, {'fields': (('name',),)}), ('Admin', {'fields': ('slug', 'uuid', 'created')}))
    """
    fieldsets = (
        *BaseKaosModelAdmin.fieldsets[:-1],
        SluggedKaosModelAdminBlock.the_admin_fieldset,
    )


class BaseBasicSluggedKaosModelAdminExtra(BaseKaosModelAdmin):
    """
    `BaseBasicSluggedKaosModelAdmin` with extra admin fields (modified)

    :param fieldsets: ((None, {'fields': (('name',),)}),
        ('Admin', {'fields': ('slug', 'uuid', 'created', 'modified')}))
    """
    fieldsets = (
        *BaseBasicSluggedKaosModelAdmin.fieldsets[:-1],
        SluggedKaosModelAdminBlock.the_admin_fieldset_extra,
    )


class BaseSluggedKaosModelAdmin(EnhancedSluggedKaosModelAdminMixin, BaseBasicSluggedKaosModelAdmin):
    """
    Base model admin for `SluggedKaosModel`.

    This admin has the enhancements for slug like prepopulate, edit readonly or being unrequired.

    :param edit_readonly_fields: ('slug',)
    :param slug_field: 'slug'
    :param slug_source: 'name'
    """


class BaseSluggedKaosModelAdminExtra(EnhancedSluggedKaosModelAdminMixin, BaseBasicSluggedKaosModelAdminExtra):
    """
    `BaseSluggedKaosModelAdmin`  with extra admin fields (modified)

    :param fieldsets: ((None, {'fields': (('name',),)}),
        ('Admin', {'fields': ('slug', 'uuid', 'created', 'modified')}))
    """


__all__ = (
    'BaseKaosModelAdmin',
    'BaseKaosModelAdminExtra',
    'BaseBasicSluggedKaosModelAdmin',
    'BaseBasicSluggedKaosModelAdminExtra',
    'BaseSluggedKaosModelAdmin',
    'BaseSluggedKaosModelAdminExtra',
)
