def egg_count(display_value):
    egg = 0
    for i in decimal_to_binary(display_value):
        if int(i):
            egg +=1
    return egg

def decimal_to_binary(num):
    result = []
    n = num
    while n > 0:
        result.append(str(n%2))
        n//=2

    result.reverse()
    return "".join(result)
        