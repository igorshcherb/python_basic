"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in args]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    """
    функция, которая на вход принимает число
    и определяет, является ли оно простым

    >>> is_prime(12)
    <<< False
    >>> is_prime(11)
    <<< True
    """
    if num in (0, 1):
        return False
    else:
        divider = 2
        while divider * divider <= num and num % divider != 0:
            divider += 1
        return divider * divider > num

def is_odd(in_num):
    """
        функция, которая на вход принимает число
        и определяет, является ли оно нечетным

    """
    if(in_num % 2) != 0:
        return True
    else:
        return False

def is_even(in_num):
    """
        функция, которая на вход принимает число
        и определяет, является ли оно четным

    """
    if(in_num % 2) == 0:
        return True
    else:
        return False

def filter_numbers(nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    >>> filter_numbers([2, 3, 4, 5], PRIME)
    <<< [2, 3, 5]
    """
    if filter_type == ODD:
            return list(filter(is_odd, nums))
    elif filter_type == EVEN:
            return list(filter(is_even, nums))
    elif filter_type == PRIME:
            return list(filter(is_prime, nums))

