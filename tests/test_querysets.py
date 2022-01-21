import pytest

from sample.models import ArchivableHasUUID, PublishableHasUUID

pytestmark = pytest.mark.django_db


def test_ArchivableQueryset():
    active = ArchivableHasUUID.objects.create()
    archived = ArchivableHasUUID.objects.create()
    archived.archive()
    archived.save()

    # active()
    assert active in ArchivableHasUUID.objects.active()
    assert archived not in ArchivableHasUUID.objects.active()

    # archived()
    assert active not in ArchivableHasUUID.objects.archived()
    assert archived in ArchivableHasUUID.objects.archived()


def test_PublishableQueryset():
    draft = PublishableHasUUID.objects.create()
    published = PublishableHasUUID.objects.create()
    published.publish()
    published.save()
    archived = PublishableHasUUID.objects.create()
    archived.archive()
    archived.save()

    # draft()
    assert draft in PublishableHasUUID.objects.draft()
    assert published not in PublishableHasUUID.objects.draft()
    assert archived not in PublishableHasUUID.objects.draft()

    # published()
    assert draft not in PublishableHasUUID.objects.published()
    assert published in PublishableHasUUID.objects.published()
    assert archived not in PublishableHasUUID.objects.published()

    # active()
    assert draft not in PublishableHasUUID.objects.active()
    assert published in PublishableHasUUID.objects.active()
    assert archived not in PublishableHasUUID.objects.active()

    # archived()
    assert draft not in PublishableHasUUID.objects.archived()
    assert published not in PublishableHasUUID.objects.archived()
    assert archived in PublishableHasUUID.objects.archived()
