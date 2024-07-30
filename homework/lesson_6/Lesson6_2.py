z = list(range(1, 101))
print(z)
c = []

for x in z:
    if (x % 3 == 0 and x % 5 == 0):
        x = 'FuzzBuzz'
        c.append(x)

    elif x % 3 == 0:
        o = 'Fuzz'
        c.append(o)

    elif x % 5 == 0:
        p = 'Buzz'
        c.append(p)
    else:
        c.append(x)
for i in c:
    print(i)
