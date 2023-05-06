def calculator():
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        'mod': lambda x, y: x % y,
        'pow': lambda x, y: x ** y,
        'div': lambda x, y: x // y
    }

    try:
        num_1 = float(input('Input first number: '))
        num_2 = float(input('Input second number: '))
        operation = input('Input math operation: ')
        for operator in ops:
            if operation == operator:
                return f'answer = {ops[operation](num_1, num_2)}'

    except ValueError:
        return 'Incorrect value!'
    except ZeroDivisionError:
        return 'Divided by zero!'
    return 'Error!'


print(calculator())
