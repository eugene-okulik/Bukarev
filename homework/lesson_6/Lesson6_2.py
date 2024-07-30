z = list(range(1, 101))
print(z)
c = []

#Числа кратные трем
for x in z:
    if (x % 3 == 0 and x % 5 == 0):
        x = 'FuzzBuzz'
        c.append(x)

    elif x % 3 == 0:
        #print(x, end=' ')
        o = 'Fuzz'
        c.append(o)

    elif x % 5 == 0:
        #print(x, end=' ')
        p = 'Buzz'
        c.append(p)
    else:
        c.append(x)
for i in c:
    print(i)
    