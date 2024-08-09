def operacii(func):

    def wrapper(first, second):
        if first < 0:
            operation = '*'
            func(first, second, operation)
        if second < 0:
            operation = '*'
            func(first, second, operation)
        elif first == second:
            operation = '+'
            func(first, second, operation)
        elif first > second:
            operation = '-'
            func(first, second, operation)
        elif second > first:
            operation = '/'
            func(first, second, operation)
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
        return first * second


calc(10, 10)
