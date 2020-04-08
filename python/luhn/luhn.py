class Luhn:
    def __init__(self, card_num):
        self._card_num = card_num

    def valid(self):

        digits = ''.join(self._card_num.split())

        if not digits.isdigit() or len(digits) <= 1:
            return False

        sum_digit = 0

        for index, num in enumerate(digits[::-1]):
            num = int(num)

            if index % 2 != 0:
                num *= 2
                if num > 9:
                    num -= 9

            sum_digit += num

        return sum_digit % 10 == 0
