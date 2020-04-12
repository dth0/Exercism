import re

from string import ascii_lowercase


def is_pangram(sentence):
    letters = "".join(
        [s.lower() for s in re.findall(r'[a-z]+', sentence, re.IGNORECASE)]
    )

    return len(set(letters)) == len(ascii_lowercase)
