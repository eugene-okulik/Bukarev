def operacii(func):

    def wrapper(first, second):
        if first < 0:
            operation = '*'
            print(func(first, second, operation))
        if second < 0:
            operation = '*'
            print(func(first, second, operation))
        elif first == second:
            operation = '+'
            print(func(first, second, operation))
        elif first > second:
            operation = '-'
            print(func(first, second, operation))
        elif second > first:
            operation = '/'
            print(func(first, second, operation))
    return wrapper


@operacii
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first + second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return print(first * second)
calc(10, 10)
