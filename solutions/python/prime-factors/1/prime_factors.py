
def factors(n):
    d = 2
    result = []
    while d <= n:
        if n % d == 0:
            n = n // d
            result.append(d)
        else:
            d+=1
    
    return result
        