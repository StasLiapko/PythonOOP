from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCard(PaymentMethod):
    def make_payment(self, amount):
        print(f"Payment of {amount} made using Credit Card.")

class BankTransfer(PaymentMethod):
    def make_payment(self, amount):
        print(f"Payment of {amount} made using Bank Transfer.")

class EWallet(PaymentMethod):
    def make_payment(self, amount):
        print(f"Payment of {amount} made using E-Wallet.")

class PaymentProcessor:
    def __init__(self):
        self.payment_methods = []

    def add_payment_method(self, payment_method):
        self.payment_methods.append(payment_method)

    def process_payment(self, amount, method_index):
        if 0 <= method_index < len(self.payment_methods):
            payment_method = self.payment_methods[method_index]
            payment_method.make_payment(amount)
        else:
            print("Invalid payment method index.")


 
credit_card = CreditCard()
bank_transfer = BankTransfer()
e_wallet = EWallet()
  
payment_processor = PaymentProcessor()

payment_processor.add_payment_method(credit_card)
payment_processor.add_payment_method(bank_transfer)
payment_processor.add_payment_method(e_wallet)

payment_processor.process_payment(100, 0)  
payment_processor.process_payment(150, 1)  
payment_processor.process_payment(200, 2)  