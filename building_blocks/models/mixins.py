from building_blocks.utils import create_initials


class HasInitials:
    take_initials_from = None

    @property
    def initials(self):
        if self.take_initials_from is None:
            raise AttributeError(f"take_initials_from not defined on {self.__class__}")
        return create_initials(getattr(self, self.take_initials_from))
