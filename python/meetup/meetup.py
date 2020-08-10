import calendar


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):

    m_list = calendar.Calendar().monthdatescalendar(year, month)

    weekday = eval(f"calendar.{day_of_week.upper()}")

    list_of_days = [w[weekday] for w in m_list if w[weekday].month == month]

    if week[0].isdigit():
        try:
            rval = list_of_days[int(week[0])-1]
        except IndexError:
            raise MeetupDayException("This day doesn't exist!")
    elif week == "teenth":
        for w in list_of_days:
            if 10 <= w.day < 20:
                rval = w
    elif week == "last":
        rval = list_of_days[-1]

    return rval
