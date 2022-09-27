from simple.models import Product


def test_UnnamedKaosModel():
    pass


def test_KaosModel():
    pass


def test_SluggedKaosModel(db):
    product = Product.objects.create(name="Name", price=10)
    assert product.uuid
    assert product.created
    assert product.slug == 'name'

    assert str(product.uuid).startswith(product.shortcode)
