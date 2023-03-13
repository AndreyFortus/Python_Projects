# Multi-paradigm programming languages, Task №3
# Andrey Fortus IKM-221a
import math

GENERAL_INFO = 'Multi-paradigm programming languages, Task №3'
STUDENT_INFO = 'Andrey Fortus IKM-221a'
TEMPLATE = 'Input {} value: '

# info
print(GENERAL_INFO)
print(STUDENT_INFO)

# Math
while True:
    try:
        x = float(input(TEMPLATE.format('x')))
        z = float(input(TEMPLATE.format('z')))
        if z - pow(x, 3) / 3 == 0:
            print("z - pow(x, 3) / 3 shouldn't equal zero !")
        elif pow(z, 2) - math.fabs(pow(x, 2) / (z - pow(x, 3) / 3)) == 0:
            print("pow(z, 2) - math.fabs(pow(x, 2) / (z - pow(x, 3) / 3))) shouldn't equal zero!")
    except ValueError:
        print('Value Error! Try again!')
    else:
        try:
            y = z + x / (pow(z, 2) - math.fabs(pow(x, 2) / (z - pow(x, 3) / 3)))
            print(f'y = {y}')
            break
        except ZeroDivisionError:
            print('Division by zero ! Try another value')