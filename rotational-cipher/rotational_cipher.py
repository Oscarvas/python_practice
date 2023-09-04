def rotate(text, key):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plain = ''.join([letter + letter.upper() for letter in alphabet]) # "aA" + "bB" + "cC" + ...
    
    cipher = plain[key*2:] + plain[:key*2]

    sentence = [word.translate(str.maketrans(plain, cipher)) for word in text.split()]
    
    return ' '.join(sentence)
