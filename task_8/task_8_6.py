def year(param_year):
    if param_year > 3000 or param_year < 1900:
        return 'Program works only in 1900 - 3000 values of year'
    if param_year % 4 == 0 and (param_year % 400 == 0 or param_year % 100 != 0):
        return 'Leap year'
    return 'Ordinary year'


print(year(2104))
