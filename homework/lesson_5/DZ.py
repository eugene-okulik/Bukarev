symbol = '='
symbol *= 40

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)
print(name)

z = 'результат операции: 42'
d = 'результат операции: 514'
f = 'результат работы программы: 9'
list_z = z.split()
list_d = d.split()
list_f = f.split()
print(symbol)
print(list_z)
print('Индекс = ', list_z.index('42'))
per_z = int(list_z[2])+10
print(per_z)
print(symbol)

print('Индекс = ', list_d.index('514'))
per_d = int(list_d[2])+10
print('Результат сложеия = ', per_d)
print(symbol)

print('Индекс = ', list_f.index('9'))
per_f = int(list_f[3])+10
print('Результат сложеия = ', per_f)
print(symbol)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print(', '.join(students) + 'study these subjects: ' + ', '.join(subjects))




