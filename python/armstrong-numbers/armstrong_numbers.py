import math


def is_armstrong_number(number):
    if number:
        count = math.ceil(math.log10(number))

    result = 0
    calc_num = number
    while calc_num:
        result += (calc_num % 10) ** count
        calc_num = calc_num // 10

    return result == number
