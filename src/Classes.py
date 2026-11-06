class Product:


    def __init__(self, name: str, description: str, price: float | int, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products

    def product_count(self) -> int:
        return len(self.products)

    def category_count(self) -> int:

        return sum([p.quantity for p in self.products])