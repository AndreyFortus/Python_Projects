import numpy as np


def check_numbers(number, list_num_with_ends):
    if number == 1:
        list_num_with_ends.append(f'{number}st')
    elif number == 2:
        list_num_with_ends.append(f'{number}nd')
    elif number == 3:
        list_num_with_ends.append(f'{number}rd')
    else:
        list_num_with_ends.append(f'{number}th')


def numbers(list_num):
    list_num_with_ends = []
    for number in list_num:
        check_numbers(number, list_num_with_ends)
    return list_num_with_ends


list_num = np.arange(1, 10, 1)
print(numbers(list_num))
