from building_blocks.admin import BaseAdminBlock, AdminBlock, HasUUIDAdminBlock, HasSlugAdminBlock, \
    TimeStampedAdminBlock, UnnamedBaseKaosModelAdminBlock, KaosModelAdminBlock, SluggedKaosModelAdminBlock, \
    ArchivableAdminBlock, ArchivableAdminFilter
from building_blocks.consts.field_names import UUID, SLUG, CREATED, MODIFIED, NAME


def test_BaseAdminBlock():
    assert BaseAdminBlock.base_fields is None
    assert BaseAdminBlock.extra_fields is None
    assert BaseAdminBlock.admin_fields is None
    assert BaseAdminBlock.extra_admin_fields is None
    assert BaseAdminBlock.readonly_fields is None
    assert BaseAdminBlock.extra_readonly_fields is None
    assert BaseAdminBlock.edit_readonly_fields is None
    assert BaseAdminBlock.extra_edit_readonly_fields is None
    assert BaseAdminBlock.autocomplete_fields is None
    assert BaseAdminBlock.extra_autocomplete_fields is None

    assert BaseAdminBlock.the_fieldset is None
    assert BaseAdminBlock.the_fieldset_extra is None
    assert BaseAdminBlock.the_admin_fieldset is None
    assert BaseAdminBlock.the_admin_fieldset_extra is None


def test_AdminBlock():
    assert AdminBlock.actions is None
    assert AdminBlock.extra_actions is None
    assert AdminBlock.search_fields is None
    assert AdminBlock.extra_search_fields is None
    assert AdminBlock.list_display is None
    assert AdminBlock.extra_list_display is None
    assert AdminBlock.list_filter is None
    assert AdminBlock.extra_list_filter is None


def test_HasUUIDAdminBlock():
    assert HasUUIDAdminBlock.readonly_fields == (UUID,)
    assert HasUUIDAdminBlock.admin_fields == (UUID,)
    assert HasUUIDAdminBlock.the_admin_fieldset == ("Admin", {'fields': HasUUIDAdminBlock.admin_fields})


def test_HasSlugAdminBlock():
    assert HasSlugAdminBlock.admin_fields == (SLUG,)
    assert HasSlugAdminBlock.edit_readonly_fields == (SLUG,)


def test_TimeStampedAdminBlock():
    assert TimeStampedAdminBlock.readonly_fields == (CREATED, MODIFIED)
    assert TimeStampedAdminBlock.admin_fields == (CREATED,)
    assert TimeStampedAdminBlock.extra_admin_fields == (MODIFIED,)
    assert TimeStampedAdminBlock.the_admin_fieldset_extra == ("Admin", {
        'fields': TimeStampedAdminBlock.admin_fields + TimeStampedAdminBlock.extra_admin_fields
    })


def test_UnnamedBaseKaosModelAdminBlock():
    assert UnnamedBaseKaosModelAdminBlock.admin_fields == (UUID, CREATED,)
    assert UnnamedBaseKaosModelAdminBlock.extra_admin_fields == (MODIFIED,)
    assert UnnamedBaseKaosModelAdminBlock.readonly_fields == (UUID, CREATED, MODIFIED,)


def test_KaosModelAdminBlock():
    assert KaosModelAdminBlock.admin_fields == (UUID, CREATED,)
    assert KaosModelAdminBlock.base_fields == (NAME,)
    assert KaosModelAdminBlock.extra_admin_fields == (MODIFIED,)
    assert KaosModelAdminBlock.readonly_fields == (UUID, CREATED, MODIFIED)
    assert KaosModelAdminBlock.the_fieldset == (None, {'fields': KaosModelAdminBlock.base_fields})


def test_SluggedKaosModelAdminBlock():
    assert SluggedKaosModelAdminBlock.admin_fields == (SLUG, UUID, CREATED,)
    assert SluggedKaosModelAdminBlock.base_fields == (NAME,)
    assert SluggedKaosModelAdminBlock.extra_admin_fields == (MODIFIED,)
    assert SluggedKaosModelAdminBlock.readonly_fields == (UUID, CREATED, MODIFIED)
    assert SluggedKaosModelAdminBlock.the_fieldset == (None, {'fields': KaosModelAdminBlock.base_fields})


def test_ArchivableAdminBlock():
    assert ArchivableAdminBlock.actions == ('archive', 'restore')
    assert ArchivableAdminBlock.admin_fields == ('is_available',)
    assert ArchivableAdminBlock.extra_admin_fields == ('is_archived',)
    assert ArchivableAdminBlock.list_display == ('is_available',)
    assert ArchivableAdminBlock.list_filter == (ArchivableAdminFilter,)
    assert ArchivableAdminBlock.extra_list_display == ('is_archived',)
    assert ArchivableAdminBlock.readonly_fields == ('is_available', 'is_archived')
