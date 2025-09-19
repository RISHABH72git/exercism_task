def square_of_sum(number):
    count = 0
    for i in range(1, number+1):
        count += i
    return count ** 2


def sum_of_squares(number):
    count = 0
    for i in range(1, number+1):
        count += i ** 2
    return count

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
