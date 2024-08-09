def repeat_me(func):

    def wrapper(*args, count1):
        i = 0
        while i < count1:
            func(*args)
            i += 1
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count1=10)
