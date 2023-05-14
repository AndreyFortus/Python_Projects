def int_checker():
    try:
        number = int(input('Input your number: '))
        return number
    except ValueError:
        print('Your input is incorrect! Must be integer value.')
