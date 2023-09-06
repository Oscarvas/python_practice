INPUT_CHARS = '[{('
OUTPUT_CHARS = ']})'

def is_paired(input_string: str) -> bool:

    my_stack = []
    
    for char in input_string:
        if char in INPUT_CHARS:
            my_stack.append(char)
        elif char in OUTPUT_CHARS:
            
            # if stack is empty or the last element in the stack is not the corresponding opening bracket
            if not my_stack or INPUT_CHARS.index(my_stack.pop()) != OUTPUT_CHARS.index(char): 
                return False
        else:
            continue

    return not my_stack # the stack should be empty if all brackets are paired
