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
    
    def __add__(self, other):
        if not isinstance(other, Client):
            raise TypeError("Unsupported operand type(s) for +: 'Client' and '{}'".format(type(other)))
        return self.get_total_price([]) + other.get_total_price([])
    
    def __iter__(self):
        return iter(self.orders)  

    def __getitem__(self, index):
        return self.orders[index]  