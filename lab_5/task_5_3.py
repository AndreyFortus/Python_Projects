# Multi-paradigm programming languages, task №5.3
# Andrey Fortus IKM-221a

# Square root function
def square_root(start_value):
    x_value = start_value
    while abs(x_value * x_value - start_value) > 1e-8:
        x_value = (x_value + start_value / x_value) / 2
    return round(x_value, 3)


GENERAL_INFO = 'Multi-paradigm programming languages, task №5.3'
STUDENT_INFO = 'Andrey Fortus IKM-221a variant №20'

# info
print(GENERAL_INFO)
print(STUDENT_INFO)


# find square root
def main():
    try:
        n_value = float(input('Input value: '))
    except ValueError:
        print('Value must not be string!')
    else:
        if n_value < 0:
            raise ValueError('value must be equal or greater than 0')
        print(f'Square {n_value} equal {square_root(n_value)}')
