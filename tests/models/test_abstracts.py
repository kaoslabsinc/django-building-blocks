import pytest

from simple.models import Product


def test_Archivable__raises(db):
    product = Product.objects.create(name="Name", price=10)

    with pytest.raises(AssertionError):
        product.restore()

    product.archive()
    product.save()
    with pytest.raises(AssertionError):
        product.archive()
