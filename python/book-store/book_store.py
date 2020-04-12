from collections import Counter


DISCOUNT = {
    5: 0.25,
    4: 0.20,
    3: 0.10,
    2: 0.05,
    1: 0
}

PRICE = 800


def get_descont(books):
    real_price = PRICE * books
    return int(real_price - (DISCOUNT[books] * real_price))


def total(basket):
    c = Counter(basket)

    groups = []
    while sum(c.values()):
        count = 0
        for index in c.keys():
            if c[index]:
                c[index] -= 1
                count += 1

        groups.append(count)

    rep_num = min(groups.count(3), groups.count(5))

    for _ in range(rep_num):
        groups[groups.index(3)] += 1
        groups[groups.index(5)] -= 1

    return sum([get_descont(x) for x in groups])
