import calendar


def is_leap_year_v1(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def find_leap_year_v2(year):
    result = False
    if calendar.isleap(year):
        result = True
    return result

