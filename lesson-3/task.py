"""
Homework for the lesson #3
"""

from math import sqrt, pow
import operator


def power(*args, power=2):
    """ Accepts numbers as separate arguments """

    def p(x):
        return x ** power

    # lst = list(map(lambda x: pow(x, power), args))
    # lst = [pow(x, power) for x in args]
    lst = list(map(p, args))

    return lst


def is_prime(n):
    """ checks if a number is prime """

    if n < 2:
        return False
    if n == 2:
        return True
        
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1

    return True


def filter_func(numbers, is_even, is_prime=False):
    if is_even:
        filtered_nums = [i for i in numbers if i % 2 == 0]
    else:
        filtered_nums = [i for i in numbers if i % 2 != 0]

    return filtered_nums

if __name__ == '__main__':
    print(power(1, 4, 5))
    print(power(1, 4, 5, power=4))

    print(filter_func([1, 4, 6, 8, 9], True))
    print(filter_func([1, 4, 6, 8, 9], False))