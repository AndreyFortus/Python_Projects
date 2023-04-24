def money():
    nominal_list = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    person_list = ['Volodimir The Great', 'Yaroslav the Wise', 'Bohdan Khmelnytsky',
                   'Ivan Mazepa', 'Ivan Mazepa', 'Mykhailo Hrushevskyi',
                   'Taras Shevchenko', 'Lesia Ukrainka', 'Hryhorii Skovoroda', 'Volodymyr Vernadskyi']
    try:
        nominal = int(input('Input nominal: '))
        for i in range(len(nominal_list)):
            if nominal == nominal_list[i]:
                return f'{person_list[i]} is depicted on {nominal_list[i]} hryvnias'
            return 'Nominal not found. Try another'
    except ValueError:
        return 'Incorrect nominal! Try again'


print(money())
