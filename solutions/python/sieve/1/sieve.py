def primes(limit):
    prime_numbers = []
    for i in range(1,limit+1):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers

def is_prime(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count == 2