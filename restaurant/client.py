from discount import Discount
class Client:
    """This class represents clients"""
    def __init__(self, name: str, discount: Discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order):
        total_price = sum(dish.price for dish in order)
        return self.discount.apply_discount(total_price)

    def create_order(self, *dishes):
        return list(dishes)