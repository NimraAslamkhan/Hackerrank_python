# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def validate_credit_card(card):
   
    pattern = re.compile(r"^[456]\d{3}(-?\d{4}){3}$")
    
    
    if not pattern.match(card):
        return "Invalid"
    
   
    card_digits = card.replace('-', '')
    
    
    if re.search(r"(\d)\1{3,}", card_digits):
        return "Invalid"
    
    return "Valid"