def month_check():
    month_list = ['january', 'march', 'april', 'may', 'june',
                  'july', 'august', 'september', 'october', 'november', 'december']
    days_list = [31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while True:
        month = input('Input month for more info: ')
        for i in range(len(month_list)):
            if month.lower() == month_list[i]:
                return f'in {month} {days_list[i]} days'
            elif month.lower() == 'february':
                try:
                    year = int(input('Input year: '))
                    if year % 4 == 0:
                        return f' in {year} in {month} 29 days'
                    return f'in {year} in {month} 28 days'
                except ValueError:
                    print('Try input correct year!')
        print('Try input correct month!')


print(month_check())
