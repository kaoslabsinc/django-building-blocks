import pytest
from django_fsm import TransitionNotAllowed

from simple.models import Product, ProductStatusArchivable, ProductPublishable


def test_Archivable__raises(db):
    product = Product.objects.create(name="Name", price=10)

    with pytest.raises(AssertionError):
        product.restore()

    product.archive()
    product.save()
    with pytest.raises(AssertionError):
        product.archive()


def test_StatusArchivable__raises(db):
    product = ProductStatusArchivable.objects.create(name="Name", price=10)

    with pytest.raises(TransitionNotAllowed):
        product.restore()

    product.archive()
    product.save()
    with pytest.raises(TransitionNotAllowed):
        product.archive()


def test_Publishable__raises(db):
    product = ProductPublishable.objects.create(name="Name", price=10)

    with pytest.raises(TransitionNotAllowed):
        product.restore()

    product.archive()
    with pytest.raises(TransitionNotAllowed):
        product.archive()

    product.restore()
    product.publish()
    with pytest.raises(TransitionNotAllowed):
        product.publish()

    product.unpublish()
    with pytest.raises(TransitionNotAllowed):
        product.unpublish()

