import calendar

def feature4_v1(year):
    if len(str(year))==4:
        if year % 4 != 0:
            return "Обычный"
        elif year % 100 == 0:
            if year % 400 == 0:
                return "Високосный"
            else:
                return "Обычный"
        else:
            return "Високосный"
    else:
        return "Число не четырехзначное"

def feature4_v2(year):
    if len(str(year)) == 4:
        if calendar.isleap(year):
            return "Високосный"
        else:
            return "Обычный"
    else:
        return "Число не четырехзначное"
