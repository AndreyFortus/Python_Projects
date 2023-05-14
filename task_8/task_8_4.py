def check_num():
    while True:
        try:
            num = int(input())
            return f'{num} is even' if num % 2 == 0 else f'{num} is odd'

        except ValueError:
            print('Incorrect value. Try again!')


print(check_num())
