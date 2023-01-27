from building_blocks.consts.field_names import *
from .base import *
from ..utils import combine_admin_blocks_factory

UnnamedBaseKaosModelAdminBlock = combine_admin_blocks_factory(
    HasUUIDAdminBlock,
    TimeStampedAdminBlock
)
SluggedKaosModelAdminBlock = combine_admin_blocks_factory(
    HasSlugAdminBlock,
    UnnamedBaseKaosModelAdminBlock
)


class KaosModelAdminBlock(UnnamedBaseKaosModelAdminBlock):
    base_fields = (
        NAME,
    )
    the_fieldset = (None, {'fields': base_fields})


__all__ = (
    'UnnamedBaseKaosModelAdminBlock',
    'KaosModelAdminBlock',
    'SluggedKaosModelAdminBlock',
)
