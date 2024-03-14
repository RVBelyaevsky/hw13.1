
class Category:
    title: str
    description: str
    products: list

    count_categories = 0
    unique_products = 0
    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.products = products
        self.count_categories = 1

        Category.count_categories += 1


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

