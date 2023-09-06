import re

OPERATIONS = ['plus','minus','multiplied', 'divided']

def answer(question: str) -> int:

    clean = re.sub(r"[a-zA-Z\s?]","",question)

    # let's find the first number given
    try:
        index = question.find(clean[0])
    except:
        if question.lower().startswith("what"):
            raise ValueError("syntax error")
        else:
            raise ValueError("unknown operation")

    equation = question[index:-1].split()

    if len(equation) == 1: # iteration 0 - only 1 digit
        return int(clean)
    

    result = int(equation[0])

    while "by" in equation: # second cleanup
        equation.remove("by")
        
    if any(not digit.replace('-','').isdigit() if not i%2 \
           else digit.replace('-','').isdigit() \
           for i, digit in enumerate(equation)): 
        raise ValueError("syntax error")

    for i, digit in enumerate(equation[1:],1):
        
        if not digit.replace('-','').isdigit() and \
            digit in OPERATIONS:
            continue

        if equation[i-1] == 'plus': # iteration 1
            result+= int(digit)
        
        elif equation[i-1] == 'minus':
            result-= int(digit)
        
        elif equation[i-1] == 'multiplied':
            result*= int(digit)
        
        elif equation[i-1] == 'divided':
            result/= int(digit)
        else:
            raise ValueError("unknown operation")
        
    if equation[-1] in OPERATIONS:
        raise ValueError("syntax error")
    
    return result