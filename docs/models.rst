Models
======

Models
------

.. autoclass:: building_blocks.models.KaosModel
   :show-inheritance:

.. autoclass:: building_blocks.models.UnnamedKaosModel
   :show-inheritance:

.. autoclass:: building_blocks.models.SluggedKaosModel
   :show-inheritance:


Mixins
------

.. autoclass:: building_blocks.models.HasUUIDModel
   :show-inheritance:

.. autoclass:: building_blocks.models.NamedModel
   :show-inheritance:

.. autoclass:: building_blocks.models.SluggedModel
   :show-inheritance:

.. autoclass:: building_blocks.models.OrderableModel
   :show-inheritance:

.. autoclass:: building_blocks.models.Orderable0Model
   :show-inheritance:

Base
----

.. autoclass:: building_blocks.models.UnnamedBaseKaosModel
   :show-inheritance:

.. autoclass:: building_blocks.models.BaseKaosModel
   :show-inheritance:


Abstracts
---------

.. autoclass:: building_blocks.models.Archivable
   :members: archive, restore
   :show-inheritance:

.. autoclass:: building_blocks.models.StatusArchivable
   :members: archive, restore
   :show-inheritance:

.. autoclass:: building_blocks.models.Publishable
   :members: archive, restore, publish, unpublish
   :show-inheritance:

QuerySets
---------

.. autoclass:: building_blocks.models.ArchivableQuerySet
   :members: available, archived, set_archived, set_restored
   :show-inheritance:


.. autoclass:: building_blocks.models.StatusArchivableQuerySet
   :members: available, archived, set_archived, set_restored
   :show-inheritance:

.. autoclass:: building_blocks.models.PublishableQuerySet
   :members: available, archived, published, set_archived, set_restored, set_published, set_unpublished
   :show-inheritance:
