Admin blocks
************

.. contents::
    :local:
    :depth: 2

.. automodule:: building_blocks.admin.blocks

Bases
=====
.. autoclass:: building_blocks.admin.blocks.base.BaseAdminBlock

.. autoclass:: building_blocks.admin.blocks.base.AdminBlock
    :show-inheritance:

Implementations
===============
.. autoclass:: building_blocks.admin.blocks.base.HasUUIDAdminBlock
    :show-inheritance:

.. autoclass:: building_blocks.admin.blocks.base.HasSlugAdminBlock
    :show-inheritance:

.. autoclass:: building_blocks.admin.blocks.base.TimeStampedAdminBlock
    :show-inheritance:

.. py:class:: UnnamedBaseKaosModelAdminBlock

    AdminBlock for models extending `UnnamedBaseKaosModel`

    :param admin_fields: (UUID, CREATED)
    :param extra_admin_fields: (MODIFIED,)
    :param readonly_fields: (UUID, CREATED, MODIFIED,)

.. autoclass:: building_blocks.admin.blocks.extra.KaosModelAdminBlock
    :show-inheritance:

.. py:class:: SluggedKaosModelAdminBlock

    AdminBlock for models extending both `SluggedModel` and `UnnamedBaseKaosModel`

    :param admin_fields: (SLUG, UUID, CREATED)
    :param base_fields: (NAME,)
    :param edit_readonly_fields: (SLUG,)
    :param extra_admin_fields: (MODIFIED,)
    :param readonly_fields: (UUID, CREATED, MODIFIED,)
    :param the_fieldset: (None, {'fields': (NAME,)})

Utils
=====
.. autoclass:: building_blocks.admin.blocks.base.AdminFieldsetTitle
