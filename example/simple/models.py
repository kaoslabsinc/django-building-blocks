from dj_kaos_utils.models import MoneyField

from building_blocks.models import SluggedKaosModel, Archivable, StatusArchivable, Publishable


class Product(Archivable, SluggedKaosModel):
    price = MoneyField()


class ProductStatusArchivable(StatusArchivable, SluggedKaosModel):
    price = MoneyField()


class ProductPublishable(Publishable, SluggedKaosModel):
    price = MoneyField()
