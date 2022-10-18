from dj_kaos_utils.models import MoneyField

from building_blocks.models import SluggedKaosModel, Archivable, StatusArchivable


class Product(Archivable, SluggedKaosModel):
    price = MoneyField()


class ProductStatusArchivable(StatusArchivable, SluggedKaosModel):
    price = MoneyField()
