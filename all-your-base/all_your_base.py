def rebase(input_base: int, digits: list, output_base: int) -> list:
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any([ d < 0  or d >= input_base for d in digits]):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    first_transform = 0
    for index, d in enumerate(digits):
        first_transform += d * input_base ** (len(digits) - index - 1)

    if first_transform == 0:
        return [0]
    
    result = []
    while first_transform > 0:
        result.append(first_transform % output_base)
        first_transform //= output_base
    
    result.reverse() 
    # returns None because it's an in-place operation
    # so we need to return the result of the operation

    return result # could be written as return result[::-1]