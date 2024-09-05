import os
import csv
import dotenv
import mysql.connector as mysql


base_path = os.path.dirname(__file__)
address_to_eu = os.path.dirname(os.path.dirname(__file__))
file_eu_okulik = os.path.join(address_to_eu, 'eugene_okulik', 'lesson_16', 'hw_data', 'data.csv')
print(file_eu_okulik)

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_DATABASE')
)


cursor = db.cursor(dictionary=True)
cursor.execute('''SELECT s.name, s.second_name, g.title group_title, b.title book_title, ss.title subject_title,
l.title lesson_title, m.value mark_value
FROM students s JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets ss ON l.subject_id = ss.id''')
data = cursor.fetchall()
# print(data)

csv_data = []
with open(file_eu_okulik, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    for row in file_data:
        csv_data.append(row)


for row in csv_data:
    print(row)


def sravnenie(data_row, csv_row):
    return (
        data_row['name'] == csv_row[0] and
        data_row['second_name'] == csv_row[1] and
        data_row['group_title'] == csv_row[2] and
        data_row['book_title'] == csv_row[3] and
        data_row['subject_title'] == csv_row[4] and
        data_row['lesson_title'] == csv_row[5] and
        str(data_row['mark_value']) == csv_row[6]
    )


missing_data = []
for csv_row in csv_data:
    found = False
    for data_row in data:
        if sravnenie(data_row, csv_row):
            found = True
            break
    if not found:
        missing_data.append(csv_row)

if missing_data:
    print('\n\n\n', "Данных не хватает в базе данных:", '\n')
    for row in missing_data:
        print(row)
else:
    print("Все данные из файла присутствуют в базе данных.")
