

def repeat_me(count1):
    def actual(func):
        def wrapper(*args):
            i = 0
            while i < count1:
                func(*args)
                i += 1
        return wrapper
    return actual


@repeat_me(count1=2)
def example(text):
    print(text)

example('print me')
