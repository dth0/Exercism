import re


def count_words(sentence):
    stg = {}
    regex = re.compile(r"([a-z\d']+)")

    for word in regex.findall(sentence.lower()):
        word = word.strip("'")

        if word not in stg:
            stg[word] = 0

        stg[word] += 1

    return stg
