resistor_colors = ["black","brown", "red", "orange", "yellow", "green", "blue", "violet","grey", "white"]
def value(colors):
    result = ""
    for color_name in range(2):
        result += str(resistor_colors.index(colors[color_name]))
    return int(result)
