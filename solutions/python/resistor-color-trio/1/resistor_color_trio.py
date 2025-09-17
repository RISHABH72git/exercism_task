registor_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
def label(colors):
    result = ""
    for i in range(3):
        if i == 2:
            for j in range(registor_colors.index(colors[i])):
                result += "0"
        else:
            result += str(registor_colors.index(colors[i]))

    unit = " "
    result = int(result)
    if result > 1000000000:
        result = result // 1000000000
        result = f"{result}"
        unit = " giga"
    elif result > 1000000:
        result = result // 1000000
        result = f"{result}"
        unit = " mega"
    elif result > 1000:
        result = result // 1000
        result = f"{result}"
        unit = " kilo"
    
    return f"{result}{unit}ohms"
