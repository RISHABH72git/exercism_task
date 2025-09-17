registor_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
tolerance_band = {
    "grey" : "±0.05%",
    "violet" : "±0.1%",
    "blue" : "±0.25%",
    "green" : "±0.5%",
    "brown" : "±1%",
    "red" : "±2%",
    "gold" : "±5%",
    "silver":"±10%"
}
def resistor_label(colors):
    if len(colors) == 1:
        b1 = registor_colors.index(colors[0])
        return f"{b1} ohms"
    elif len(colors) == 5:
        b1 = registor_colors.index(colors[0])
        b2 = registor_colors.index(colors[1])
        b3 = registor_colors.index(colors[2])
        b4 = registor_colors.index(colors[3])
        tolerance = tolerance_band[colors[4]]
        band_value = (b1 *100) + (b2 *10) + b3
        band_value = band_value * (10 ** b4)
    else:
        b1 = registor_colors.index(colors[0])
        b2 = registor_colors.index(colors[1])
        b3 = registor_colors.index(colors[2])
        tolerance = tolerance_band[colors[3]]
        band_value = (b1 *10) + b2
        band_value = band_value * (10 ** b3)

    unit = "ohms"
    if band_value >= 1_000_000_000:
        res = band_value / 1_000_000_000
        unit = f'{res:g} giga{unit} {tolerance}'
    elif band_value >= 1_000_000:
        res = band_value / 1_000_000
        unit = f'{res:g} mega{unit} {tolerance}'
    elif band_value >= 1_000:
        res = band_value / 1_000
        unit = f'{res:g} kilo{unit} {tolerance}'
    else:
        unit = f"{band_value} {unit} {tolerance}"

    return unit
    
