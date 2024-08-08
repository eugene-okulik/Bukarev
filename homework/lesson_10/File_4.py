def operacii(func):

    def wrapper(first, second, operation=None):
        if first < 0:
            return print(first * second)
        if second < 0:
            return print(first * second)
        elif first == second:
            return print(first + second)
        elif first > second:
            return print(first - second)
        elif second > first:
            return print(first / second)
    return wrapper


@operacii
def calc(first, second, operation=None):
    print('Test1')


calc(10, -3)
