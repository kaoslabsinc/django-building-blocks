import re


class HasInitials:
    take_initials_from = None

    @property
    def initials(self):
        if self.take_initials_from is None:
            raise AttributeError(f"take_initials_from not defined on {self.__class__}")
        return "".join(
            s[0] if s else '' for s in re.split(r"[\W_]+", getattr(self, self.take_initials_from))).upper()
