import math
from inspect import isgenerator

def prime_check(n):
    '''Перевіряє чи є число простим'''
    if n <= 1:  # Числа, які менші або дорівнюють 1 не є простими
       return False
    limit = math.isqrt(n)
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(end):
    """Генератор простих чисел до end"""
    for n in range(2, end + 1):
        if prime_check(n):
            yield n # реалізує генератор

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')