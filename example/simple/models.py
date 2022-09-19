from dj_kaos_utils.models import MoneyField

from building_blocks.models import SluggedKaosModel, Archivable


class Product(Archivable, SluggedKaosModel):
    price = MoneyField()
