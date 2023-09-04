COLOR_LEGEND = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def value(colors):
    # list comprehension of the first two colors in the list,
    # convert each element to str then join them into a string, then convert to int
    return int(''.join([ str(COLOR_LEGEND.index(code)) for code in colors[:2] ]))
