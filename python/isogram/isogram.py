def is_isogram(string):

    letters = {}

    for letter in string.lower():
        if not letter.isalpha():
            continue

        if letter in letters:
            return False

        letters[letter] = 1

    return True
