def append(list1, list2):
    return list1 + list2


def concat(lists):
    return flatter_array(lists)

def flatter_array(lists):
    result = []
    for i in lists:
        if i:
            if isinstance(i, list):
                result.extend(i)
            else:
                result.append(i)
    return result


def filter(function, list):
    result = []
    for i in list:
        if function(i):
            result.append(i)
    return result


def length(list):
    count = 0
    for i in list:
        count +=1
    return count

    
def map(function, list):
    result = []
    for i in list:
        result.append(function(i))
        
    return result


def foldl(function, list, initial):
    sum_num = initial
    for i in list:
        sum_num = function(sum_num, i)
    return sum_num


def foldr(function, list, initial):
    sum_num = initial
    for i in range(len(list)-1, -1, -1):
        sum_num = function(sum_num, list[i])
    return sum_num


def reverse(list):
    result = []
    index = len(list) - 1
    while index >= 0:
        result.append(list[index])
        index -=1
    return result
