class ArchivableInterface:
    is_archived: bool
    is_available: bool

    def archive(self, *args, **kwargs):
        raise NotImplementedError

    def restore(self, *args, **kwargs):
        raise NotImplementedError

    def unarchive(self, *args, **kwargs):
        return self.restore(*args, **kwargs)
