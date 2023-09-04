import re

def is_pangram(sentence):

    # Remove non-alphabetic characters and convert to lowercase
    sentence = re.sub(r'[^a-zA-Z]', '', sentence).lower()
       
    # Convert to set
    sentence = set(sentence)
    
    # Check if all letters are present
    return len(sentence) == 26


print(is_pangram("The quick brown fox jumps over the lazy dog."))