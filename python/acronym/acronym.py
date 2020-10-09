import re


def abbreviate(words):
    result = []

    regex = re.compile(r"([a-z']+)", re.IGNORECASE)

    for word in regex.findall(words.upper()):
        result.append(word[0].upper())

    return "".join(result)
