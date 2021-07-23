import datetime as dt
import uuid

import pytest
from django.utils.timezone import now

from building_blocks.models.enums import PublishingStage
from sample.models import HasUUIDExample, ArchivableHasUUID, PublishableHasUUID


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


def test_Publishable_publish(freezer):
    publishable = PublishableHasUUID()

    assert not publishable.is_active
    assert publishable.publishing_stage_changed_at is None

    publishable.publish()

    assert publishable.is_active
    assert publishable.publishing_stage == PublishingStage.published
    assert publishable.publishing_stage_changed_at == now()


def test_Publishable_unpublish(freezer):
    publishable = PublishableHasUUID(
        publishing_stage=PublishingStage.published,
        publishing_stage_changed_at=now() - dt.timedelta(hours=1)
    )

    assert publishable.is_active

    publishable.unpublish()

    assert not publishable.is_active
    assert publishable.publishing_stage == PublishingStage.draft
    assert publishable.publishing_stage_changed_at == now()


def test_Publishable_archive(freezer):
    publishable = PublishableHasUUID(
        publishing_stage=PublishingStage.published,
        publishing_stage_changed_at=now() - dt.timedelta(hours=1)
    )

    assert publishable.is_active

    publishable.archive()

    assert not publishable.is_active
    assert publishable.publishing_stage == PublishingStage.archived
    assert publishable.publishing_stage_changed_at == now()


def test_Publishable_restore(freezer):
    publishable = PublishableHasUUID(
        publishing_stage=PublishingStage.archived,
        publishing_stage_changed_at=now() - dt.timedelta(hours=1)
    )

    assert not publishable.is_active

    publishable.restore()

    assert not publishable.is_active
    assert publishable.publishing_stage == PublishingStage.draft
    assert publishable.publishing_stage_changed_at == now()


def test_Publishable_assertions():
    draft = PublishableHasUUID(
        publishing_stage=PublishingStage.draft,
        publishing_stage_changed_at=now() - dt.timedelta(hours=1)
    )
    published = PublishableHasUUID(
        publishing_stage=PublishingStage.published,
        publishing_stage_changed_at=now() - dt.timedelta(hours=1)
    )
    archived = PublishableHasUUID(
        publishing_stage=PublishingStage.archived,
        publishing_stage_changed_at=now() - dt.timedelta(hours=1)
    )

    # publish()
    with pytest.raises(AssertionError):
        published.publish()
    with pytest.raises(AssertionError):
        archived.publish()

    # unpublish()
    with pytest.raises(AssertionError):
        draft.unpublish()
    with pytest.raises(AssertionError):
        archived.unpublish()

    # restore()
    with pytest.raises(AssertionError):
        draft.restore()
    with pytest.raises(AssertionError):
        published.restore()
