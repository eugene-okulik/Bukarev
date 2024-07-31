symbol = '='
symbol *= 40
z = 'результат операции: 42'
d = 'результат операции: 514'
f = 'результат работы программы: 9'
w = []


def rez(*args):
    for elem in args:
        g = (elem.index(':')) + 2
        h = int((elem[g:])) + 10
        print(h)
        print(symbol)


rez(z, d, f)
