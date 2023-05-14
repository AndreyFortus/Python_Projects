from utils import int_checker


def count_numbers():
    count = 0
    while True:
        try:
            num = int_checker()
            count += num
            if num == 0:
                return count
        except ValueError:
            print('Your input is incorrect! Must be integer value.')


print(count_numbers())
