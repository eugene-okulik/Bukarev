def gen_f(line=100):
    count1 = 0
    a = 0
    b = 1
    while count1 < line:
        yield a
        a = b - a
        b = a + b
        count1 += 1


count = 1
for ff in gen_f(1000000):
    if count == 5:
        print(ff)
    elif count == 200:
        print(ff)
    elif count == 1000:
        print(ff)
    elif count == 100000:
        print(ff)
        break
    count += 1
