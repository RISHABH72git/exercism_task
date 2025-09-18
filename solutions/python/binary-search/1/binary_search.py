def find(search_list, value):
    left = 0
    right = len(search_list) 

    while left < right:
        mid = (right + left) // 2
        
        if search_list[mid] == value:
            return mid
            
        if search_list[mid] > value:
            right = mid
        else:
            left = mid +1

    raise ValueError("value not in array")