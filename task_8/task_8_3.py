import numpy as np


def check_numbers(number):
    if number == 1:
        return f'{number}st'
    elif number == 2:
        return f'{number}nd'
    elif number == 3:
        return f'{number}rd'
    else:
        return f'{number}th'


def numbers(list_num):
    list_num_with_ends = [check_numbers(number) for number in list_num]
    return list_num_with_ends

def main():
    list_numbers = np.arange(1, 10, 1)
    print(numbers(list_numbers))


main()
