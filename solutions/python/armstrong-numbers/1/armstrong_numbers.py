def is_armstrong_number(number):
    num = str(number)
    num_lenth = len(num)
    sum_number = 0
    for i in num:
        sum_number += (int(i)**num_lenth)

    return sum_number == number
