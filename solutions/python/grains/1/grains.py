def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
        
    if number == 1:
        return 1
        
    previous = 1
    for i in range(1, number):
        previous = previous*2
    return previous

def total():
    return 2 ** 64 - 1