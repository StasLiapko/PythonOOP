from product import Product

class Cart:
    def __init__(self):
        self.__quantity = []
        self.__products = []

    def add_product(self, product: 'Product', quantity = 1):
        if not isinstance(product, Product):
            raise TypeError("Product must be a Product object.")
        if not isinstance(quantity, (int, float)):
            raise TypeError("Quantity must be a number.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        self.__products.append(product)
        self.__quantity.append(quantity)

    def __str__(self) -> str:
        return f"Cart with {sum(self.__quantity)} items."

    def __iadd__(self, other):
        if not isinstance(other, Cart):
            raise TypeError("Can only combine with another Cart object.")

        self.__products.extend(other.__products)
        self.__quantity.extend(other.__quantity)
        return self
    
    def __iter__(self):
        return iter(self.__products)