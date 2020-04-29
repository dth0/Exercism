def is_valid(isbn):
    isbn_number = []

    count = 10

    for item in isbn:

        if not item.isalnum():
            continue

        if count == 1 and item.upper() == 'X':
            isbn_number.append(10 * 1)
        elif item.isdigit():
            isbn_number.append(int(item) * count)

        count -= 1

    if len(isbn_number) != 10:
        return False

    return sum(isbn_number) % 11 == 0
