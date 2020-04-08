class Clock:
    def __init__(self, hour, minute):
        self._minute = minute % 60
        self._hour = ((hour % 24) + (minute // 60 % 24)) % 24

    def __repr__(self):
        return f"{self._hour:02}:{self._minute:02}"

    def __eq__(self, other):
        return self.__repr__() == str(other)

    def __add__(self, minutes):
        self._clock_calc(minutes)
        return self

    def __sub__(self, minutes):
        self._clock_calc(minutes * -1)
        return self

    def _clock_calc(self, length):
        hour = self._hour + (length // 60)
        minute = self._minute + (length % 60)
        hour += minute // 60

        self._minute = minute % 60
        self._hour = hour % 24
