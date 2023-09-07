import string

def rows(letter: str):
    index = string.ascii_uppercase.index(letter.upper())

    template = ' ' * (index +1)

    diamond = list()

    for i, letr in enumerate(string.ascii_uppercase[:index+1]):
        aux = list(template)
        aux[i] = str(letr)
        diamond.append(''.join(aux)[::-1] + ''.join(aux[1:]) )

    return diamond + diamond[::-1][1:]
