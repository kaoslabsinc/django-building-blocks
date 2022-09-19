from dj_kaos_utils.admin import NoViewInlineMixin, NoAddInlineMixin, NoChangeInlineMixin


class AddInlineMixin(NoViewInlineMixin):
    """
    Mixin for inline admin classes. Used to create an inline that is used only as the form interface for the inline
    model. Primarily used alongside :class:`ListInlineMixin` to create edit_readonly fields for an admin
    """


class ListInlineMixin(NoViewInlineMixin):
    """
    Mixin for inline admin classes. Used to create an inline that is used to view objects, or change them, but not add
    new ones. Primarily used alongside :class:`AddInlineMixin` to create edit_readonly fields for an admin
    """


class ReadOnlyInlineMixin(NoAddInlineMixin, NoChangeInlineMixin):
    """
    Mixin for inline admin classes to create a readonly inline admin.
    """


__all__ = [
    'AddInlineMixin',
    'ListInlineMixin',
    'ReadOnlyInlineMixin',
]
