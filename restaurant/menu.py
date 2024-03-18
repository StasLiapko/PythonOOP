from exception import PriceError
class Dish:
    """This class represents dishes"""
    def __init__(self, name: str, price: float):
        if price <= 0:
            raise PriceError()
        self.name = name
        self.price = price
    
    def __str__(self) -> str:
        return f'{self.name} - {self.price} $'

class Category:
    """This class represents menu category"""
    def __init__(self, name: str):
        self.name = name
        self.__dishes = []

    def add_dish(self, dish: Dish):
        self.__dishes.append(dish)
    
    def __str__(self) -> str:
        return f'{self.name}: \n' + '\n'.join(map(str, self.__dishes))

class Menu:
    """This class represents restaurant's menu"""
    def __init__(self, name):
        self.name = name
        self.__categories = []
    
    def add_category(self, category: Category):
        self.__categories.append(category)

    def __str__(self):
        return f'{self.name} : \n' + '\n'.join(map(str, self.__categories))



