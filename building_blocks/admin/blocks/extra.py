from building_blocks.consts.field_names import *
from .base import *
from ..utils import combine_admin_blocks_factory

UnnamedBaseKaosModelAdminBlock = combine_admin_blocks_factory(
    HasUUIDAdminBlock,
    TimeStampedAdminBlock
)


class KaosModelAdminBlock(UnnamedBaseKaosModelAdminBlock):
    """
    AdminBlock for models extending `KaosModel`

    :param admin_fields: (UUID, CREATED)
    :param base_fields: (NAME,)
    :param extra_admin_fields: (MODIFIED,)
    :param readonly_fields: (UUID, CREATED, MODIFIED,)
    :param the_fieldset: (None, {'fields': (NAME,)})
    """
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
