import re

def is_valid(isbn):
    
    isbn = isbn.replace('-', '')

    # format is 9 digits plus one check character (either a digit or an X only)
    match = re.match(r'^\d{9}[0-9X]$', isbn)

    if match is None:
        return False
    
    is_valid = 0

    # could use list comprehension here, but I think this is more readable
    for index, digit in enumerate(isbn):
        if digit == 'X':
            is_valid += 10 * (10 - index)
        else:
            is_valid += int(digit) * (10 - index)
    
    return is_valid % 11 == 0
