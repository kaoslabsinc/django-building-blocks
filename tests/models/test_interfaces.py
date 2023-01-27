import pytest

from building_blocks.models.interfaces import ArchivableInterface, ArchivableQuerySetInterface


class TestArchivableInterface:
    @pytest.fixture
    def instance(self):
        return ArchivableInterface()

    @pytest.fixture
    def instance_inherited(self):
        class Model(ArchivableInterface):
            def restore(self, *args, **kwargs):
                self.some_value = 1

        return Model()

    def test_archive_not_implemented(self, instance):
        with pytest.raises(NotImplementedError):
            instance.archive()

    def test_restore_not_implemented(self, instance):
        with pytest.raises(NotImplementedError):
            instance.restore()

    def test_unarchive_not_implemented(self, instance):
        with pytest.raises(NotImplementedError):
            instance.unarchive()

    def test_unarchive_calls_restore(self, instance_inherited):
        with pytest.raises(AttributeError):
            getattr(instance_inherited, 'some_value')
        instance_inherited.unarchive()
        assert instance_inherited.some_value == 1


class TestArchivableQuerySetInterface:
    @pytest.fixture
    def instance(self):
        return ArchivableQuerySetInterface()

    def test_set_archived_not_implemented(self, instance):
        with pytest.raises(NotImplementedError):
            instance.set_archived()

    def test_set_restored_not_implemented(self, instance):
        with pytest.raises(NotImplementedError):
            instance.set_restored()
