def square_root(number):
    low, high = 1, number
    while low <= high:
        mid = (low + high) //2
        sq = mid * mid 
        if sq == number:
            return mid

        if sq > number:
            high = mid 
        else:
            low = mid +1
    return 0
        
