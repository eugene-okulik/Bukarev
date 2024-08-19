import os
import datetime

base_path = os.path.dirname(__file__)
address_to_eu = os.path.dirname(os.path.dirname(__file__))
file_eu_okulik = os.path.join(address_to_eu, 'eugene_okulik', 'hw_13', 'data.txt')
new_file_path = os.path.join(base_path, 'data2.txt')
print(file_eu_okulik)
print(file_eu_okulik)

time_now = datetime.datetime.now()
# print(time_now)
time_1 = str(time_now).split(' ')
# print(time_1)
# print(type(time_1))


def read_file():
    with open(file_eu_okulik, encoding="utf-8") as data_file:
        print(data_file)
        for line in data_file.readlines():
            yield line.strip()


for data_line in read_file():
    with (open(new_file_path, 'a', encoding="utf-8") as new_file):
        z = data_line.split()
        # print(z)
        # print(len(z))
        if z[0] == '1.':
            z_1 = data_line.split()[1] + ' ' + data_line.split()[2]
            z_3 = datetime.datetime.strptime(z_1, '%Y-%m-%d %H:%M:%S.%f')
            s = z_3 + datetime.timedelta(weeks=1)
            z_4 = datetime.datetime.strftime(s, '%Y-%m-%d %H:%M:%S.%f ')
            z.append('Результат: ' + z_4)
            new_file.write(' '.join(z) + "\n")

        elif z[0] == '2.':
            z_1 = data_line.split()[1] + ' ' + data_line.split()[2]
            z_3 = datetime.datetime.strptime(z_1, '%Y-%m-%d %H:%M:%S.%f')
            z_4 = datetime.datetime.strftime(z_3, '%A')
            z.append('Результат: ' + z_4)
            new_file.write(' '.join(z) + "\n")

        elif z[0] == '3.':
            z_1 = data_line.split()[1] + ' ' + data_line.split()[2]
            z_2 = datetime.datetime.strptime(z_1, '%Y-%m-%d %H:%M:%S.%f')
            date_old = (time_now - z_2)
            day = date_old.days
            z.append('Результат: ' + str(day) + ' дней назад')
            new_file.write(' '.join(z) + "\n")

            # print(str(z))




        # print(z_with_newline)
        # print(type(z_with_newline))
        #
        # new_file.write(z_with_newline)
        # # print(type(z))
