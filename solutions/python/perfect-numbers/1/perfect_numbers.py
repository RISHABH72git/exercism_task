def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    divisor_list = [i for i in range(1, number) if number % i == 0]
    sum_divisor_list = sum(divisor_list)
    if number == sum_divisor_list:
        return "perfect"
    elif number > sum_divisor_list:
        return "deficient"
    else:
        return "abundant"

        
    