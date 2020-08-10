"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from collections import Counter


# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 10
FOUR_OF_A_KIND = 20
LITTLE_STRAIGHT = -30
BIG_STRAIGHT = 30
CHOICE = -1


def choice(dice):
    return sum([k * v for k, v in dice.items()])


def yacht(dice):
    if len(dice) == 1:
        return YACHT

    return 0


def big_straight(dice):
    return BIG_STRAIGHT if straight(dice, 1) else 0


def little_straight(dice):
    return -LITTLE_STRAIGHT if straight(dice, 6) else 0


def straight(dice, excluded):
    return len(dice) == 5 and dice[excluded] == 0


def full_house(dice):
    if len(dice) == 2:
        for num in dice.keys():
            if num in [2, 3]:
                return choice(dice)

    return 0


def four_of_a_kind(dice):
    for k, v in dice.items():
        if v >= 4:
            return k * 4

    return 0


data = {
    YACHT: yacht,
    FULL_HOUSE: full_house,
    FOUR_OF_A_KIND: four_of_a_kind,
    LITTLE_STRAIGHT: little_straight,
    BIG_STRAIGHT: big_straight,
    CHOICE: choice
}


def score(dice, category):
    numbers = Counter(dice)

    if 1 <= category <= 6:
        return category * numbers.get(category, 0)
    else:
        func = data.get(category)

        return func(numbers)
