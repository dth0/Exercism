from string import ascii_lowercase

bucket = {char:pos for pos, char in enumerate(ascii_lowercase)}

def rotate(text, key):

    result = []

    for char in text:
        if char.lower() not in bucket:
            result.append(char)
            continue

        pos = (bucket[char.lower()] + key) % len(ascii_lowercase)
        new_char = ascii_lowercase[pos]

        result.append(new_char if char.islower() else new_char.upper())

    return "".join(result)
