from building_blocks.consts.field_names import *
from .base import *
from ..utils import combine_admin_blocks_factory

UnnamedBaseKaosModelAdminBlock = combine_admin_blocks_factory(
    HasUUIDAdminBlock,
    TimeStampedAdminBlock
)


class KaosModelAdminBlock(UnnamedBaseKaosModelAdminBlock):
    base_fields = (
        NAME,
    )
    the_fieldset = (None, {'fields': base_fields})


SluggedKaosModelAdminBlock = combine_admin_blocks_factory(
    HasSlugAdminBlock,
    KaosModelAdminBlock
)

__all__ = (
    'UnnamedBaseKaosModelAdminBlock',
    'KaosModelAdminBlock',
    'SluggedKaosModelAdminBlock',
)
