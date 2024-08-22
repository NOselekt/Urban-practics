from typing import Callable
import random

def is_prime(number: int):
    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            return False
    return True

def is_prime_decorator(func: Callable):
    def wrapper(*numbers: int):
        result = func(*numbers)
        if is_prime(result):
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper



@is_prime_decorator
def my_sum(*numbers: int):
    result = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            print('В список чисел затесался импостер')
    return result


a = [random.randint(100000, 1000000) for i in range(1000000)]
print(my_sum(*a))

result = my_sum(2, 3, 6)
print(result)