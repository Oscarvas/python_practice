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
                byte = aux[-7:]

                byte = '1' + '0'*(7-len(byte)) + byte \
                    if len(aux) != len(vlq) else byte
                
                aux_encode.append(int(byte,2)) # specific base
                aux = aux[:-7] # reduce aux size
            
            result.extend(aux_encode[::-1]) # extend with the inverted list

    return result

def decode(bytes_: list) -> list:
    pass
