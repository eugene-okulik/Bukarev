

def repeat_me(count1):
    def actual(func):
        def wrapper(*args):
            print(f'функция "repeat_me" вызывалась {count1} раз: ', *args * count1, sep='\n')
        return wrapper
    return actual


@repeat_me(count1=4)
def example(text):
    print(text)


example('print me')
