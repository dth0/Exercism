def decode(string):
    digit = []
    result = []

    for char in string:

        if char.isdigit():
            digit.append(char)
        else:
            num = int("".join(digit)) if digit else 1
            digit = []

            result.append(char * num)

    return "".join(result)


def encode(string):

    make_string = lambda c, l: f"{c}{l}" if c > 1 else l

    if not string:
        return ""

    result = []

    l_index = 0

    for r_index, letter in enumerate(string):

        if string[l_index] != letter:
            result.append(make_string(r_index - l_index, string[l_index]))
            l_index = r_index

    result.append(make_string(r_index - l_index + 1, string[l_index]))

    return "".join(result)
