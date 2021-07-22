import uuid

from sample.models import HasUUIDExample


def test_HasUUID():
    # UUID('8f95b2d0-9fe9-4250-b134-bcf377e33f24')
    bytes = b'\x8f\x95\xb2\xd0\x9f\xe9BP\xb14\xbc\xf3w\xe3?$'
    u = uuid.UUID(bytes=bytes)
    has_uuid = HasUUIDExample(uuid=u)

    assert has_uuid.uuid_str == '8f95b2d0-9fe9-4250-b134-bcf377e33f24'
    assert has_uuid.shortcode == '8f95b2d0'
