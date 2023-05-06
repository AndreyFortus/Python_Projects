# Multi-paradigm programming languages, Task №4
# Andrey Fortus IKM-221a

GENERAL_INFO = 'Multi-paradigm programming languages, Task №4'
STUDENT_INFO = 'Andrey Fortus IKM-221a'

# info
print(GENERAL_INFO)
print(STUDENT_INFO)


# function for Fibonacci numbers
def fibonacci(n_value):
    if n_value == 0:
        return 0
    if n_value < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# print n is the number of Fibonacci numbers
n = int(input('Input number of Fibonacci numbers: '))
if n <= 0:
    raise ValueError('n must be more then 0')

print('Fibonacci numbers: ')
fib_list = [fibonacci(i) for i in range(n)]
print(fib_list)
