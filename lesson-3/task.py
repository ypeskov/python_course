"""
Homework for the lesson #3
"""

from math import sqrt, pow
# import operator
from functools import wraps
from time import time
from itertools import repeat


def timer(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        time_start = time()
        result = f(*args, **kwargs)
        time_end = time()
        print('%s() took: %f sec' % (f.__name__, time_end-time_start))

        return result

    return wrapped


@timer
def power1(*args, power=2):
    def p(x):
        return x ** power

    lst = list(map(p, args))
    return lst


@timer
def power2(*args, power=2):
    return [pow(x, power) for x in args]


@timer
def power3(*args, power=2):
    return list(map(lambda x: pow(x, power), args))


@timer
def power4(*args, power=2):
    return(list(map(pow, args, repeat(power))))


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


def filter_func1(numbers, filter_type):
    IS_EVEN = 'even'
    IS_ODD = 'odd'
    IS_PRIME = 'prime'

    if filter_type == IS_EVEN:
        # filtered_nums = [i for i in numbers if i % 2 == 0]
        filtered_nums = list(filter(lambda i: i % 2 == 0, numbers))
    elif filter_type == IS_ODD:
        filtered_nums = [i for i in numbers if i % 2 != 0]
    elif filter_type == IS_PRIME:
        filtered_nums = [i for i in numbers if is_prime(i)]
    else:
        raise ValueError('Unknown filter type')

    return filtered_nums


def filter_func2(numbers, filter_type):
    """ compact variant of the filter function """

    funcs = {
        'even': lambda i: i % 2 == 0,
        'odd': lambda i: i % 2 != 0,
        'prime': lambda i: is_prime(i)
    }

    return list(filter(funcs[filter_type], numbers))


if __name__ == '__main__':
    nums = [5, 3, 5] * 10_000_000
    power1(*nums, power=5)
    power2(*nums, power=5)
    power3(*nums, power=5)
    power4(*nums, power=5)

    # print(filter_func1([1, 4, 6, 8, 9], 'even'))
    # print(filter_func2([1, 4, 6, 8, 9], 'even'))
    # print(filter_func2([1, 4, 6, 8, 9], 'odd'))
    # print(filter_func2([1, 2, 3, 4, 5, 6, 8, 9], 'prime'))