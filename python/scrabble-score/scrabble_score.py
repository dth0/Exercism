from collections import Counter


def score(word):
    result = 0

    letter_scores = {
        "AEIOULNRST": 1,
        "DG": 2,
        "BCMP": 3,
        "FHVWY": 4,
        "K": 5,
        "JX": 8,
        "QZ": 10,
    }

    word_count = Counter(word.upper())

    for letter, total in word_count.items():
        for letter_score in letter_scores:
            if letter in letter_score:
                result += (letter_scores[letter_score] * total)

    return result
