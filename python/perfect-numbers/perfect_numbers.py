def classify(number):

    if number < 1:
        raise ValueError("Number cannot be less than one")

    result = 0
    for num in range(1, number):
        if number % num == 0:
            result += num

    if result == number:
        return "perfect"
    elif result > number:
        return "abundant"
    else:
        return "deficient"
