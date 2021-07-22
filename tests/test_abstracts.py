import uuid

from django.utils.timezone import now

from sample.models import HasUUIDExample, ArchivableHasUUID


def test_HasUUID():
    # UUID('8f95b2d0-9fe9-4250-b134-bcf377e33f24')
    bytes = b'\x8f\x95\xb2\xd0\x9f\xe9BP\xb14\xbc\xf3w\xe3?$'
    u = uuid.UUID(bytes=bytes)
    has_uuid = HasUUIDExample(uuid=u)

    assert has_uuid.uuid_str == '8f95b2d0-9fe9-4250-b134-bcf377e33f24'
    assert has_uuid.shortcode == '8f95b2d0'


def test_Archivable_archive():
    archivable = ArchivableHasUUID()

    assert archivable.is_active
    assert archivable.archive_status == 'active'

    archivable.archive()

    assert not archivable.is_active
    assert archivable.archive_status == 'archived'


def test_Archivable_restore():
    archivable = ArchivableHasUUID(archived_at=now())

    assert not archivable.is_active
    assert archivable.archive_status == 'archived'

    archivable.restore()

    assert archivable.is_active
    assert archivable.archive_status == 'active'
