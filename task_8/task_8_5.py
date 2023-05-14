from task_8_6 import year_check


def month_check():
    month_dict = {
        'january': 31, 'march': 31, 'may': 31, 'july': 31, 'august': 31, 'october': 31, 'december': 31,
        'april': 30, 'june': 30, 'september': 30, 'november': 30
    }
    while True:
        month = input('Input month for more info: ')
        if month.lower() in month_dict:
            return f'in {month} {month_dict[month]} days'
        if month.lower() == 'february':
            year = int(input('Input year: '))
            return year_check(year)


print(month_check())
