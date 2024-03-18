from product import Product
from cart import Cart
from exception import MoneyError
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

if __name__ == "__main__":
    try:
        pr_1 = Product("Phone", 1)
        pr_2 = Product("Laptop", 500)
        pr_3 = Product("Tablet", 300)

        cart_1 = Cart()
        cart_2 = Cart()
        cart_1.add_product(pr_1, 3)
        cart_2.add_product(pr_2, 1)
        cart_1.add_product(pr_3, 3)
        cart_1 += cart_2

        print(cart_1)
        
        for product, quantity in cart_1:
            print(product, quantity)
    except Exception as e:
        logger.exception("Exception occurred")