import re

def validate_login(login):
    pattern = r'^[a-zA-Z0-9]{2,10}$'
    
    if re.match(pattern, login):
        return True
    else:
        return False

login = "user7312"
if validate_login(login):
    print("Login is valid.")
else:
    print("Invalid login.")