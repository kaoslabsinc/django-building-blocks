import uuid

import pytest
from django_fsm import TransitionNotAllowed

from building_blocks.models.abstracts import Orderable
from building_blocks.models.enums import PublishingStatus, ArchiveStatus
from sample.models import HasUUIDExample, ArchivableHasUUID, PublishableHasUUID, OrderedStuff


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
    assert archivable.status == ArchiveStatus.active

    archivable.archive()

    assert not archivable.is_active
    assert archivable.status == ArchiveStatus.archived


def test_Archivable_restore():
    archivable = ArchivableHasUUID()
    archivable.archive()

    assert not archivable.is_active
    assert archivable.status == ArchiveStatus.archived

    archivable.restore()

    assert archivable.is_active
    assert archivable.status == ArchiveStatus.active


def test_Publishable_publish(freezer):
    publishable = PublishableHasUUID()

    assert not publishable.is_active

    publishable.publish()

    assert publishable.is_active
    assert publishable.status == PublishingStatus.published


def test_Publishable_unpublish(freezer):
    publishable = PublishableHasUUID()
    publishable.publish()

    assert publishable.is_active

    publishable.unpublish()

    assert not publishable.is_active
    assert publishable.status == PublishingStatus.draft


def test_Publishable_archive(freezer):
    publishable = PublishableHasUUID()
    publishable.publish()

    assert publishable.is_active

    publishable.archive()

    assert not publishable.is_active
    assert publishable.status == PublishingStatus.archived


def test_Publishable_restore(freezer):
    publishable = PublishableHasUUID()
    publishable.archive()

    assert not publishable.is_active

    publishable.restore()

    assert not publishable.is_active
    assert publishable.status == PublishingStatus.draft


def test_Publishable_assertions():
    draft = PublishableHasUUID()
    published = PublishableHasUUID()
    published.publish()
    archived = PublishableHasUUID()
    archived.archive()

    # publish()
    with pytest.raises(TransitionNotAllowed):
        published.publish()
    with pytest.raises(TransitionNotAllowed):
        archived.publish()

    # unpublish()
    with pytest.raises(TransitionNotAllowed):
        draft.unpublish()
    with pytest.raises(TransitionNotAllowed):
        archived.unpublish()

    # restore()
    with pytest.raises(TransitionNotAllowed):
        draft.restore()
    with pytest.raises(TransitionNotAllowed):
        published.restore()


def test_Publishable_first_published_at(db):
    publishable = PublishableHasUUID.objects.create()
    publishable.publish()
    publishable.save()
    assert publishable.first_published_at
    first_published_at = publishable.first_published_at

    publishable.unpublish()
    publishable.save()
    assert publishable.first_published_at
    assert publishable.first_published_at == first_published_at

    publishable.publish()
    publishable.save()
    assert publishable.first_published_at
    assert publishable.first_published_at == first_published_at

    publishable.archive()
    publishable.save()
    assert publishable.first_published_at
    assert publishable.first_published_at == first_published_at

    publishable.restore()
    publishable.save()
    assert publishable.first_published_at
    assert publishable.first_published_at == first_published_at

    publishable.publish()
    publishable.save()
    assert publishable.first_published_at
    assert publishable.first_published_at == first_published_at


def test_Orderable(db):
    obj1 = OrderedStuff.objects.create(name="asd")
    obj2 = OrderedStuff.objects.create(name="asd2")
    assert obj1.order == obj2.order == Orderable.DEFAULT_ORDER

    qs = OrderedStuff.objects.all()
    assert qs.first() == obj1
    assert qs.last() == obj2

    obj2.order = 1
    obj2.save()
    qs = OrderedStuff.objects.all()
    assert qs.first() == obj2
    assert qs.last() == obj1
