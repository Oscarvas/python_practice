def encode(numbers: list) -> list:

    result = []

    for number in numbers:
        as_int = int(number)
        if (as_int < 128):
            result.append(number)
        
        else:
            vlq = bin(as_int)[2:] ## remove starting 0b..
            aux, aux_encode = vlq, []

            while aux:
                byte = aux[-7:] # get last 7 bits

                byte = '1' + '0'*(7-len(byte)) + byte \
                    if len(aux) != len(vlq) else byte # only the first 7-bits (from right) is 0xxxxxxx
                
                aux_encode.append(int(byte,2)) # specific base
                aux = aux[:-7] # reduce aux size
            
            result.extend(aux_encode[::-1]) # extend with the inverted list

    return result

def decode(bytes_: list) -> list:
    result = []
    
    bits = ''

    for number in bytes_:
        clean_number = bin(number)[2:][-7:]  # extract 0b first, then get last 7 bits

        if number > 127:
            bits += clean_number
        
        else:
            bits += '0'*(7-len(clean_number)) + clean_number
            result.append(int(bits,2))
            bits = ''

    if bits:
        raise ValueError("incomplete sequence")

    return result