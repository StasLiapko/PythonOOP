class BalanceDescriptor:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
    
    def __get__(self, instance, owner):
        return self._balance
    
    def __set__(self, instance, value):
        raise AttributeError("Modification of balance is not allowed")


class Account:
    balance = BalanceDescriptor()  

    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    def __setattr__(self, attr, value):
        if attr == 'balance':
            raise AttributeError("Modification of balance is not allowed")
        super().__setattr__(attr, value)
    
    def __getattr__(self, attr):
        if attr == 'balance':
            return self.balance
        else:
            raise AttributeError(f"Account object has no attribute '{attr}'")



account = Account(100)
print(account.balance)  

try:
    account.balance = 200  
except AttributeError as e:
    print(e)   

try:
    print(account.noproperty) 
except AttributeError as e:
    print(e)