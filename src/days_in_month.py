def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def days(month, year):
    if not isinstance(month, int) or not isinstance(year, int):
        return "Invalid"

    if month < 1 or month > 12:
        return "Invalid"

    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        return 29 if is_leap(year) else 28