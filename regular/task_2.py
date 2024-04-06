import re

def validate_credit_card(card_number):
    pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
    
    if re.match(pattern, card_number):
        return True
    else:
        return False

card_number = "1254-5666-9662-7777"
if validate_credit_card(card_number):
    print("Card is valid.")
else:
    print("Invalid card")