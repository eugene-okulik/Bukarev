-- создать пользователя
INSERT INTO students (name, second_name) VALUE ('Виктор10', 'Букарев10')

--создаем книгу 1
INSERT INTO books (title) VALUE ('Тест по математике')

--создаем книгу 2
INSERT INTO books (title) VALUE ('Тест по географии')

--узнаем id студента -1946 и id книг
SELECT * FROM students WHERE name = 'Виктор10' and second_name = 'Букарев10' 
SELECT * FROM  books WHERE title ='Тест по математике' OR title = 'Тест по географии'

--присваиваем книги студенту
UPDATE books SET taken_by_student_id = 1946 WHERE books.id = '3832' OR books.id = '3833'

--создать группу для студента
INSERT INTO `groups` (title, start_date, end_date) VALUE ('TEST Group for VIP student', 'march 2023', 'sept 2024')
SELECT * FROM `groups` WHERE title = 'TEST Group for VIP student'

-- Определить студента в группу
UPDATE students SET group_id = 1814  WHERE students.id = '1946'

--Создайте несколько учебных предметов (subjects)
INSERT INTO subjets (title) VALUE ('Математика_100')
INSERT INTO subjets (title) VALUE ('География_100')
SELECT * FROM subjets WHERE  title = 'География_100' OR title = 'Математика_100'

--Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons (title, subject_id) VALUE ('Урок1', 2546)
INSERT INTO lessons (title, subject_id) VALUE ('Урок2', 2546)
INSERT INTO lessons (title, subject_id) VALUE ('Урок1', 2547)
INSERT INTO lessons (title, subject_id) VALUE ('Урок2', 2547)
SELECT * FROM lessons l WHERE  title = 'Урок1' OR title = 'Урок2'

--Поставьте своему студенту оценки (marks) для всех созданных вами занятий
INSERT INTO marks (value, lesson_id, student_id) VALUE ('5', 5376, 1946)
INSERT INTO marks (value, lesson_id, student_id) VALUE ('5', 5377, 1946)
INSERT INTO marks (value, lesson_id, student_id) VALUE ('5', 5378, 1946)
INSERT INTO marks (value, lesson_id, student_id) VALUE ('5', 5379, 1946)
SELECT * FROM marks WHERE  student_id  = 1946

--Получите информацию из базы данных:

--Все оценки студента
SELECT * FROM students RIGHT JOIN marks ON students.id = marks.student_id WHERE students.id = 1946

-- Все книги, которые находятся у студента
SELECT * FROM students RIGHT JOIN books ON students.id = books.taken_by_student_id WHERE students.id = 1946



SELECT * FROM students JOIN `groups` ON students.group_id = `groups`.id
JOIN books ON students.id = books.taken_by_student_id
JOIN marks ON students.id = marks.student_id
JOIN lessons ON students.id = marks.student_id
JOIN subjets ON lessons.subject_id = subjets.id 
WHERE (`groups`.id = 1814) and (books.taken_by_student_id = 1946) AND (marks.student_id = 1946) AND (subjets.id = 2546 OR subjets.id = 2547)