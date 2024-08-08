# Задание №2
# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция
#
# Код, использующий этот декоратор может выглядеть, например, так:

def repeat_me(func):

    def wrapper(*args, count1):
        print(f'функция "repeat_me" вызывалась {count1} раз: ', *args * count1, sep='\n')
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count1=2)
