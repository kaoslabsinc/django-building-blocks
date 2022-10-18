class ArchivableInterface:
    is_archived: bool

    @property
    def is_available(self):
        return not self.is_archived

    def archive(self, *args, **kwargs):
        raise NotImplementedError

    def restore(self, *args, **kwargs):
        raise NotImplementedError

    def unarchive(self, *args, **kwargs):
        return self.restore(*args, **kwargs)
