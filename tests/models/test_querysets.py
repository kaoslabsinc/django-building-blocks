import pytest

from simple.models import Product


def test_ArchivableQuerySet(db):
    product = Product.objects.create(name="Name", price=10)
    assert Product.objects.available().count() == 1
    assert Product.objects.archived().count() == 0
    assert product.is_available is True

    product.archive()
    product.save()
    assert Product.objects.available().count() == 0
    assert Product.objects.archived().count() == 1
    assert product.is_available is False

    product.refresh_from_db()
    product.restore()
    product.save()
    assert Product.objects.available().count() == 1
    assert Product.objects.archived().count() == 0
    assert product.is_available is True


def test_ArchivableQuerySet__raises(db):
    product = Product.objects.create(name="Name", price=10)

    with pytest.raises(AssertionError):
        product.restore()

    product.archive()
    product.save()
    with pytest.raises(AssertionError):
        product.archive()
