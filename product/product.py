from exception import MoneyError
class Product:

    def __init__(self, name: str, price: float | int) -> None:
        if not isinstance(price, int | float):
            raise TypeError("Price must be a number.")
        if price <= 0:
            raise MoneyError("Price cannot be negative.")

        self.price = price
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} costs {self.price} dollars."






