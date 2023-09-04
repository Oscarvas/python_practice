import re

def is_isogram(string):
    
    # Remove all non-alphabetic characters
    string = re.sub(r'[^a-zA-Z]', '', string).lower()
    string = string.replace(' ', '').replace('-', '')
        
    return len(set(string)) == len(string)
    