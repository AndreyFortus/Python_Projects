def year(year):
    if year > 3000 or year < 1900:
        return 'Program works only in 1900 - 3000 values of year'
    elif year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return 'Leap year'
    return 'Ordinary year'


year_param = 2104
print(year(year_param))
