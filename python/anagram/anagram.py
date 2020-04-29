from collections import Counter


def find_anagrams(word, candidates):
    rval = []
    word = word.lower()
    word_counter = Counter(word)

    for candidate in candidates:
        c_word = candidate.lower()

        if c_word == word:
            continue

        if word_counter == Counter(c_word):
            rval.append(candidate)

    return rval
