COLOR_LEGEND = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

METRICS = ["","kilo", "mega", "giga"]

def label(colors: list) -> str:
    
    resistance = int(''.join([str(COLOR_LEGEND[color]) for color in colors[:2]]))
    power = COLOR_LEGEND[colors[2]]

    final_resistance = resistance * 10 ** power

    if final_resistance < 10 ** 3:
        return f"{final_resistance} {METRICS[0]}ohms"

    if final_resistance < 10 ** 6:
        return f"{int(final_resistance / 10 ** 3)} {METRICS[1]}ohms"
    
    if final_resistance < 10 ** 9:
        return f"{int(final_resistance / 10 ** 6)} {METRICS[2]}ohms"
    
    else:
        return f"{int(final_resistance / 10 ** 9)} {METRICS[3]}ohms"
    
    