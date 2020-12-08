"""
Homework for the lesson #3
"""

from math import sqrt, pow
# import operator
from functools import wraps
from time import time


def timer(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        time_start = time()
        result = f(*args, **kwargs)
        time_end = time()
        print('%s(%s, %s) took: %f sec' % (f.__name__, args, kwargs, time_end-time_start)) # noqa

        return result

    return wrapped


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


@timer
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
    print(power(1, 4, 5))
    print(power(1, 4, 5, power=4))

    print(filter_func1([1, 4, 6, 8, 9], 'even'))
    print(filter_func2([1, 4, 6, 8, 9], 'even'))
    print(filter_func2([1, 4, 6, 8, 9], 'odd'))
    print(filter_func2([1, 2, 3, 4, 5, 6, 8, 9], 'prime'))