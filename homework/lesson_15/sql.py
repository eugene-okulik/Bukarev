import mysql.connector as mysql

db = mysql.connect(
    username='st-onl',
    password='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
'''Создаем пользователя'''
query = "INSERT INTO students (name, second_name) VALUE (%s, %s)"
cursor = db.cursor()
cursor.execute(query, ('Виктор11', 'Букарев11'))
student_id = cursor.lastrowid
print('Id студента : ', student_id)

'''Создайте несколько книг (books)'''

query = "INSERT INTO books (title) VALUE (%s)"
cursor = db.cursor()
cursor.executemany(query, (['книга тест100'], ['книга тест200']))
last_id = cursor.lastrowid
count = cursor.rowcount
booksID = []
for i in range(count):
    booksID.append(last_id - count + 1 + i)
print(booksID)

'''созданный студент взял книги'''

query = "UPDATE books SET taken_by_student_id = %s WHERE books.id = %s"
cursor = db.cursor()
update_params = [(student_id, booksID[0]), (student_id, booksID[1])]
cursor.executemany(query, update_params)

'''Создайте группу (group)'''

query = "INSERT INTO `groups` (title, start_date, end_date) VALUE (%s, %s, %s)"
cursor = db.cursor()
param = [('Группа волшебства', 'май 2023', 'сентябрь 2023')]
cursor.executemany(query, param)
group_id = cursor.lastrowid

'''определите своего студента  в группу'''
query = "UPDATE students SET group_id = %s  WHERE students.id = %s"
cursor = db.cursor()
update_params_g = [(group_id, student_id)]
cursor.executemany(query, update_params_g)

'''Создайте несколько учебных предметов'''
query = "INSERT INTO subjets (title) VALUE (%s)"
cursor = db.cursor()
param_s = [('математика1',), ('математика2',)]
cursor.executemany(query, param_s)
sub_last_id = cursor.lastrowid
count1 = cursor.rowcount
sub_ID = []
for i in range(count):
    sub_ID.append(sub_last_id - count1 + 1 + i)
print(sub_ID)

'''Создайте по два занятия для каждого предмета (lessons)'''
query = "INSERT INTO lessons (title, subject_id) VALUE (%s, %s)"
cursor = db.cursor()
param_l = [('Занятие1', sub_ID[0]), ('Занятие2', sub_ID[0]), ('Занятие1', sub_ID[1]), ('Занятие2', sub_ID[1])]
cursor.executemany(query, param_l)
less_last_id = cursor.lastrowid
count2 = cursor.rowcount
les_ID = []
for i in range(count2):
    les_ID.append(less_last_id - count2 + 1 + i)
print(les_ID)

'''Поставьте своему студенту оценки (marks) для всех созданных вами занятий'''
query = "INSERT INTO marks (value, lesson_id, student_id) VALUE (%s, %s, %s)"
cursor = db.cursor()
param_m = [('5', les_ID[0], student_id),
           ('5', les_ID[1], student_id),
           ('5', les_ID[2], student_id),
           ('5', les_ID[3], student_id)]
cursor.executemany(query, param_m)
m_last_id = cursor.lastrowid
count3 = cursor.rowcount
m_ID = []
for i in range(count3):
    m_ID.append(m_last_id - count3 + 1 + i)
print(m_ID)

'''Получите информацию из базы данных:'''
'''Все оценки студента'''

query = "SELECT * FROM students RIGHT JOIN marks ON students.id = marks.student_id WHERE students.id = %s"
cursor = db.cursor()
cursor.execute(query, (student_id, ))
all_marks = cursor.fetchall()
for elem in all_marks:
    print(elem)

'''Все книги, которые находятся у студента'''
query = "SELECT * FROM students RIGHT JOIN books ON students.id = books.taken_by_student_id WHERE students.id = %s"
cursor = db.cursor()
cursor.execute(query, (student_id, ))
all_books = cursor.fetchall()
for elem in all_books:
    print(elem)

'''Для вашего студента выведите всё, что о нем есть в базе: группа, книги,
 оценки с названиями занятий и предметов (всё одним запросом с использованием Join)'''

query = '''SELECT * FROM students JOIN `groups` ON students.group_id = `groups`.id
JOIN books ON students.id = books.taken_by_student_id
JOIN marks ON students.id = marks.student_id
JOIN lessons ON students.id = marks.student_id
JOIN subjets ON lessons.subject_id = subjets.id
WHERE (`groups`.id = %s) and (books.taken_by_student_id = %s) AND (marks.student_id = %s)
AND (subjets.id = %s OR subjets.id = %s)'''
cursor = db.cursor()
param_all = (group_id, student_id, student_id, sub_ID[0], sub_ID[1])
cursor.execute(query, param_all)
result = cursor.fetchall()
for item in result:
    print(item)

db.commit()
db.close()
