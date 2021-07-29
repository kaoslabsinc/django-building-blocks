from building_blocks.utils import create_initials


class HasInitials:
    """
    Add property `initials` to its inheritor classes. Take the value form the field defined by `take_initials_from` and
    return the initial letters of each word in it, capitalized.
    Example: John Smith => JS
    """
    take_initials_from = None

    @property
    def initials(self):
        if self.take_initials_from is None:
            raise AttributeError(f"take_initials_from not defined on {self.__class__}")
        return create_initials(getattr(self, self.take_initials_from))


class HasAutoFields:
    def set_auto_fields(self):
        """Override this method to set the fields that need to be automatically set"""
        pass

    def clean(self):
        self.set_auto_fields()
        super(HasAutoFields, self).clean()

    def save(self, *args, **kwargs):
        self.set_auto_fields()
        super(HasAutoFields, self).save(*args, **kwargs)
