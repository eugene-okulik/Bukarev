symbol = '='
symbol *= 40

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)
print(name)
print(symbol)
z = 'результат операции: 42'
d = 'результат операции: 514'
f = 'результат работы программы: 9'
g = (z.index(':')) + 2
h = int((z[g:])) + 10
print(h)
print(symbol)
g = (d.index(':')) + 2
h = int((d[g:])) + 10
print(h)
print(symbol)
g = (f.index(':')) + 2
h = int((f[g:])) + 10
print(h)
print(symbol)


students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print(', '.join(students) + 'study these subjects: ' + ', '.join(subjects))
