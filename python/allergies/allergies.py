from collections import OrderedDict


class Allergies:
    def __init__(self, score):
        self._score = score % 256

        self._bucket = {
            1: "eggs",
            2: "peanuts",
            4: "shellfish",
            8: "strawberries",
            16: "tomatoes",
            32: "chocolate",
            64: "pollen",
            128: "cats",
        }

        self._lst = []

        count = 128
        s = self._score
        while count:
            d, m = divmod(s, count)
            if d == 1:
                self._lst.append(self._bucket[count])

                s = m

            count //= 2

    def allergic_to(self, item):
        return item in self._lst

    @property
    def lst(self):
        return self._lst
