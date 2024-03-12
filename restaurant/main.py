from menu import Dish
from menu import Category
from menu import Menu
from client import Client
from discount import GoldDiscount, SilverDiscount
from exception import PriceError
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('main.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

if __name__ == '__main__':
    try:
        dish_1 = Dish(name="Salad", price=12.5)
        dish_2 = Dish(name="Shrimps", price=-1)
        dish_3 = Dish(name="Pasta", price=5.5)
        dish_4 = Dish(name="Soup", price=4.5)
        dish_5 = Dish(name="Steak", price=15)
        dish_6 = Dish(name="Ice Cream", price=10)
        dish_7 = Dish(name="Cake", price=20)

        category_1 = Category(name="Appetizer")
        category_2 = Category(name="Main Course")
        category_3 = Category(name="Dessert")

        category_1.add_dish(dish_1)
        category_1.add_dish(dish_2)
        category_2.add_dish(dish_3)
        category_2.add_dish(dish_4)
        category_2.add_dish(dish_5)
        category_3.add_dish(dish_6)
        category_3.add_dish(dish_7)

        menu = Menu(name="Restaurant Menu")
        menu.add_category(category_1)
        menu.add_category(category_2)
        menu.add_category(category_3)

        client_silver = Client("Calvin", SilverDiscount())
        client_gold = Client("Britle", GoldDiscount())

        dish_1 = Dish(name="Salad", price=12.5)
        dish_2 = Dish(name="Shrimps", price=3)
        dish_3 = Dish(name="Pasta", price=5.5)
        dish_4 = Dish(name="Soup", price=22)
        dish_5 = Dish(name="Steak", price=15)
        dish_6 = Dish(name="Ice Cream", price=10)
        dish_7 = Dish(name="Cake", price=20)

        order_silver = client_silver.create_order(dish_4, dish_5)
        order_gold = client_gold.create_order(dish_6, dish_7)

        total_price_1 = client_silver.get_total_price(order_silver)
        total_price_2 = client_gold.get_total_price(order_gold)
        total_for_both = total_price_1 + total_price_2

        print(f"Total price for Silver client {client_silver.name}: {total_price_1}")
        print(f"Total price for Gold client {client_gold.name}: {total_price_2}")
        print(f"Total price for both clients is {total_for_both}")

        for order in order_silver:
            print(order)
        
    except PriceError as pe:
        print(f"PriceError: {pe}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        print("Done")
