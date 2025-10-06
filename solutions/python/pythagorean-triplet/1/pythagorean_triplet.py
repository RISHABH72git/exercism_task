import math
def triplets_with_sum(number):
    mid = number//3
    result = []
    for a in range(1, mid):
        b = (number**2 - 2*number*a) / (2*(number - a))
        if b.is_integer():
            c = number - a - int(b)
            if a<b and a*a + int(b)**2 == c*c:
                result.append([a, int(b), c])
    return result

    
def triplets_with_sum_O_n_square(number):
    mid = number//2
    result = []
    for i in range(1, mid):
        for j in range(i+1, mid):
            c = (i*i) + (j*j)
            root = math.sqrt(c)
            if root.is_integer() and number == (i+j+root):
                result.append([i,j,int(root)])
    return result