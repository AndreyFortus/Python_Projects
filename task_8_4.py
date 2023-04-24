def check_num():
    while True:
        try:
            num = int(input())
            if num % 2 == 0:
                return f'{num} is even'
            return f'{num} is odd'
        except ValueError:
            print('Incorrect value. Try again!')


print(check_num())
