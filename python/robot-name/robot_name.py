import time
import random

from string import ascii_uppercase, digits


class Robot:
    def __init__(self):
        self._generate_name()

    def _generate_name(self):
        random.seed(time.time())

        tag = ''.join(random.sample(ascii_uppercase, 2))
        number = ''.join(random.sample(digits, 3))

        self._name = f"{tag}{number}"

    @property
    def name(self):
        try:
            return self._name
        except NameError:
            self._generate_name()
            return self._name

    def reset(self):
        self._generate_name()
