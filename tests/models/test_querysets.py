from simple.models import Product, ProductStatusArchivable, ProductPublishable


def test_Archivable(db):
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


def test_Archivable__update_methods(db):
    Product.objects.create(name="Name", price=10)
    assert Product.objects.available().count() == 1
    Product.objects.all().set_archived()
    assert Product.objects.available().count() == 0
    Product.objects.all().set_restored()
    assert Product.objects.available().count() == 1


def test_StatusArchivable(db):
    product = ProductStatusArchivable.objects.create(name="Name", price=10)
    assert ProductStatusArchivable.objects.available().count() == 1
    assert ProductStatusArchivable.objects.archived().count() == 0
    assert product.is_available is True

    product.archive()
    product.save()
    assert ProductStatusArchivable.objects.available().count() == 0
    assert ProductStatusArchivable.objects.archived().count() == 1
    assert product.is_available is False

    product.refresh_from_db()
    product.restore()
    product.save()
    assert ProductStatusArchivable.objects.available().count() == 1
    assert ProductStatusArchivable.objects.archived().count() == 0
    assert product.is_available is True


def test_StatusArchivable__update_methods(db):
    ProductStatusArchivable.objects.create(name="Name", price=10)
    assert ProductStatusArchivable.objects.available().count() == 1
    ProductStatusArchivable.objects.all().set_archived()
    assert ProductStatusArchivable.objects.available().count() == 0
    ProductStatusArchivable.objects.all().set_restored()
    assert ProductStatusArchivable.objects.available().count() == 1


def test_Publishable(db):
    product = ProductPublishable.objects.create(name="Name", price=10)
    assert ProductPublishable.objects.available().count() == 1
    assert ProductPublishable.objects.archived().count() == 0
    assert ProductPublishable.objects.draft().count() == 1
    assert product.is_available is True
    assert product.is_draft is True
    assert product.is_published is False

    product.archive()
    product.save()
    assert ProductPublishable.objects.available().count() == 0
    assert ProductPublishable.objects.archived().count() == 1
    assert ProductPublishable.objects.draft().count() == 0
    assert product.is_available is False
    assert product.is_draft is False
    assert product.is_published is False

    product.refresh_from_db()
    product.restore()
    product.save()
    assert ProductPublishable.objects.available().count() == 1
    assert ProductPublishable.objects.archived().count() == 0
    assert ProductPublishable.objects.draft().count() == 1
    assert product.is_available is True
    assert product.is_draft is True
    assert product.is_published is False

    product.refresh_from_db()
    product.publish()
    product.save()
    assert ProductPublishable.objects.available().count() == 1
    assert ProductPublishable.objects.archived().count() == 0
    assert ProductPublishable.objects.published().count() == 1
    assert ProductPublishable.objects.draft().count() == 0
    assert product.is_available is True
    assert product.is_draft is False
    assert product.is_published is True

    product.refresh_from_db()
    product.unpublish()
    product.save()
    assert ProductPublishable.objects.available().count() == 1
    assert ProductPublishable.objects.archived().count() == 0
    assert ProductPublishable.objects.published().count() == 0
    assert ProductPublishable.objects.draft().count() == 1
    assert product.is_available is True
    assert product.is_draft is True
    assert product.is_published is False


def test_Publishable__update_methods(db):
    ProductPublishable.objects.create(name="Name", price=10)
    assert ProductPublishable.objects.available().count() == 1
    ProductPublishable.objects.all().set_archived()
    assert ProductPublishable.objects.draft().count() == 0
    assert ProductPublishable.objects.available().count() == 0
    ProductPublishable.objects.all().set_restored()
    assert ProductPublishable.objects.available().count() == 1
    assert ProductPublishable.objects.draft().count() == 1
    ProductPublishable.objects.all().set_published()
    assert ProductPublishable.objects.available().count() == 1
    assert ProductPublishable.objects.published().count() == 1
    assert ProductPublishable.objects.draft().count() == 0
    ProductPublishable.objects.all().set_unpublished()
    assert ProductPublishable.objects.available().count() == 1
    assert ProductPublishable.objects.published().count() == 0
    assert ProductPublishable.objects.draft().count() == 1
