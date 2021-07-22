import pytest
from django.utils.timezone import now

from sample.models import ArchivableHasUUID

pytestmark = pytest.mark.django_db


def test_ArchivableQueryset():
    active = ArchivableHasUUID.objects.create()
    archived = ArchivableHasUUID.objects.create(archived_at=now())

    # active()
    assert active in ArchivableHasUUID.objects.active()
    assert archived not in ArchivableHasUUID.objects.active()

    # archived()
    assert active not in ArchivableHasUUID.objects.archived()
    assert archived in ArchivableHasUUID.objects.archived()
