from menu import Dish
class PriceError(Exception):
    """Exception raised for invalid prices."""

    def __init__(self, message="Invalid price for dish. Price must be a positive number."):
        self.message = message
        super().__init__(self.message)