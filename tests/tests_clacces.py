import pytest
from src.category import Category
from src.product import Product


@pytest.fixture()
def test_product():
    return Product('Heart of Tarrasque', "броня.", 5200.0, 3)


def test_init(test_product):
    assert test_product.name == 'Heart of Tarrasque'

    assert test_product.description == "броня"
    assert test_product.price == 5200.0
    assert test_product.quantity == 3


@pytest.fixture()
def test_category():
    return Category("айтемы", "жир", [1, 2, 3])


def test_init_1(test_category):
    assert test_category.name == "айтемы"
    assert test_category.description == "жир"
    assert test_category.products == [1, 2, 3]
