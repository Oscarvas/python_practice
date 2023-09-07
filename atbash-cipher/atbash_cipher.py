import re

CIPHER = 'abcdefghijklmnopqrstuvwxyz'

def encode(plain_text: str) -> str:
    # First: extract all the alphanum from plain_text
    # Second: lowercase the first result
    # Third: translate using the cipher dictionary backwards and replace whitespaces
    plain_text = ''.join(re.findall(r'[a-zA-Z0-9]',plain_text))\
        .lower().translate(str.maketrans(CIPHER, CIPHER[::-1])).replace(' ','')
    
    result = ''
    while plain_text: # iterate over plain_text and extract characters in goups of 5
        result += plain_text[:5] + ' '
        plain_text = plain_text[5:]

    return (result+plain_text).strip() # remove any trailing whitespace added inside the loop


def decode(ciphered_text: str) -> str:
    return ciphered_text.translate(str.maketrans(CIPHER[::-1],CIPHER)).replace(' ','')
