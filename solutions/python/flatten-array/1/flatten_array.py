def flatten(iterable):
    return flatten_array(iterable)
        
    
def flatten_array(array):
    result = []
    for i in array:
        if i is not None:
            if isinstance(i, list):
                result.extend(flatten_array(i))
            else:
                result.append(i)
    return result