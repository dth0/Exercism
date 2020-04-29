def prime(number):

    if number < 1:
        raise ValueError("Zero is not allowed")

    current_num = 2
    count = 0

    while count <= number:
        rval = is_prime(current_num)

        if rval != -1:
            count += 1

        if count == number:
            return rval

        current_num += 1


def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            return -1

    return number
