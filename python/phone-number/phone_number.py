import re


class PhoneNumber:

    regex = r"^\+?1?[^\d]*?(?P<area_code>[2-9]\d{2})[^\d]*?(?P<exchange_code>[2-9]\d{2})[^\d]*?(?P<subscriber>\d{4})$"

    def __init__(self, number):
        self._parser(number)

    def _parser(self, number):
        re_comp = re.compile(self.regex)

        m = re_comp.match(number.strip())
        if not m:
            raise ValueError("Invalid Phone Number")

        for key, value in m.groupdict().items():
            setattr(self, key, value)

    @property
    def number(self):
        return self._format_number()

    def pretty(self):
        return self._format_number(raw=False)

    def _format_number(self, raw=True):
        try:
            if raw:
                rval = f"{self.area_code}{self.exchange_code}{self.subscriber}"
            else:
                rval = f"({self.area_code}) {self.exchange_code}-{self.subscriber}"
        except NameError:
            raise ValueError("This class was not instantiated")

        return rval
