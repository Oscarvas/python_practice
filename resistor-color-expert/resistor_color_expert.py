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
    "white": 9,
}

TOLERANCE_LEGEND = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}

def resistor_label(colors: list) -> str:
    
    if len(colors) < 2:
        return "0 ohms"
    
    values = int(''.join([str(COLOR_LEGEND[color]) for color in colors[:len(colors)-2]]))
    multiplier: int = 10 ** COLOR_LEGEND[colors[-2]]
    tolerance: float = TOLERANCE_LEGEND[colors[-1]]

    values = values * multiplier # 33 * 100 = 3300

    if values >= 10 ** 9:
        return f"{values / 10 ** 9} gigaohms ±{tolerance}%".replace(".0 ", " ")
    elif values >= 10 ** 6:
        return f"{values / 10 ** 6} megaohms ±{tolerance}%".replace(".0 ", " ")
    elif values >= 10 ** 3:
        return f"{values / 10 ** 3} kiloohms ±{tolerance}%".replace(".0 ", " ")
    else:
        return f"{values} ohms ±{tolerance}%".replace(".0 ", " ")
