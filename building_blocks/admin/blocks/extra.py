from building_blocks.consts.field_names import *
from .base import *
from ..utils import combine_admin_blocks_factory

UnnamedKaosBaseAdminBlock = combine_admin_blocks_factory(
    HasUUIDAdminBlock,
    TimeStampedAdminBlock
)
SluggedKaosModelAdminBlock = combine_admin_blocks_factory(
    HasSlugAdminBlock,
    UnnamedKaosBaseAdminBlock
)


class KaosModelAdminBlock(UnnamedKaosBaseAdminBlock):
    base_fields = (
        NAME,
    )
    the_fieldset = (None, {'fields': base_fields})


__all__ = (
    'UnnamedKaosBaseAdminBlock',
    'KaosModelAdminBlock',
    'SluggedKaosModelAdminBlock',
)
