from src.Classes import Product, Category


def test_product():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product1.price == 180000.0
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.quantity == 5

def test_category():
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                                 [product4])
    assert category2.products[0].price == 123000.0
    assert category2.products[0].name == "55\" QLED 4K"
    assert category2.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert category2.products[0].quantity == 7

