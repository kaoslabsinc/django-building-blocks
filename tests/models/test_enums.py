from building_blocks.models.enums import ArchiveStatus, PublishStatus


class TestArchiveStatus:
    def test_choices(self):
        assert ArchiveStatus.choices == [
            (ArchiveStatus.available.value, ArchiveStatus.available.label),
            (ArchiveStatus.archived.value, ArchiveStatus.archived.label),
        ]

    def test_available(self):
        assert ArchiveStatus.available == 0
        assert ArchiveStatus.available.label == "Available"

    def test_archived(self):
        assert ArchiveStatus.archived == -1
        assert ArchiveStatus.archived.label == "Archived"


class TestPublishStatus:
    def test_choices(self):
        assert PublishStatus.choices == [
            (PublishStatus.draft.value, PublishStatus.draft.label),
            (PublishStatus.published.value, PublishStatus.published.label),
            (PublishStatus.archived.value, PublishStatus.archived.label),
        ]

    def test_available(self):
        assert PublishStatus.draft == 0
        assert PublishStatus.draft.label == "Draft"

    def test_published(self):
        assert PublishStatus.published == 100
        assert PublishStatus.published.label == "Published"

    def test_archived(self):
        assert PublishStatus.archived == ArchiveStatus.archived
        assert PublishStatus.archived.label == ArchiveStatus.archived.label
