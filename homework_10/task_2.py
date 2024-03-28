class User:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    def __setattr__(self, attr, value):
        if attr in ['first_name', 'last_name']:
            raise AttributeError("Modification of first_name and last_name is not allowed")
        super().__setattr__(attr, value)
    
    def __getattr__(self, attr):
        raise AttributeError(f"User object has no attribute '{attr}'")



user = User("Alan", "Wake")
print(user.first_name)  

try:
    user.first_name = "Saga"  
except AttributeError as e:
    print(e)  

try:
    print(user.noproperty)  
except AttributeError as e:
    print(e)
    