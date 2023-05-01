def count_numbers():
    count = 0
    while True:
        try:
            num = int(input('Input your number (0 stop program!): '))
            count += num
            if num == 0:
                return count
        except ValueError:
            print('Your input is incorrect! Must be integer value.')
            

print(count_numbers())
