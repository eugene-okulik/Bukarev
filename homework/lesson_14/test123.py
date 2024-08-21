
import mysql.connector as mysql
import ast


class DB:
    def __init__(self, db_config):
        self.db = mysql.connect(**db_config)

    def close_connection(self):
        if self.db:
            self.db.close()

    def execute_query(self, query, params=None):
        cursor = self.db.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        columns = self.extract_columns(cursor)
        return result, columns

    def execute_insert(self, query, params=None):
        cursor = self.db.cursor()
        cursor.execute(query, params)
        self.db.commit()

    def extract_columns(self, cursor):
        columns = [desc[0] for desc in cursor.description]
        return columns


class ResultFormatter:
    @staticmethod
    def format_result(result, columns):
        formatted_result = []
        for row in result:
            row_strings = []
            for i in range(len(row)):
                column_name = columns[i]
                column_value = repr(row[i])
                row_strings.append(f'{column_name}: {column_value}')
            formatted_row = f"({', '.join(row_strings)})"
            formatted_result.append(formatted_row)
        return formatted_result

    @staticmethod
    def parse_row_string(row_string):
        row_string = row_string.strip("() ")
        pairs = row_string.split(", ")
        row_dict = {}
        for pair in pairs:
            key, value = pair.split(": ")
            row_dict[key] = ast.literal_eval(value)
        return row_dict

    @staticmethod
    def convert_to_dict(formatted_result):
        return [ResultFormatter.parse_row_string(row_string) for row_string in formatted_result]


def create_select(table_name, db_config, **conditions):
    db = DB(db_config)
    if db.db is not None:
        query = f"SELECT * FROM `{table_name}`"
        if conditions:
            where_clauses = [f"{key} = %s" for key in conditions]
            query += " WHERE " + " AND ".join(where_clauses)
            params = list(conditions.values())
            result, columns = db.execute_query(query, params)
            formatted_result = ResultFormatter.format_result(result, columns)
            print('\n Ответ наименование таблицы и значение: \n', formatted_result, '\n')
            dict_result = ResultFormatter.convert_to_dict(formatted_result)
            print('Преобразование списка в словарь: \n', dict_result)
            print(type(dict_result))
        db.close_connection()
    else:
        print('Не удалось подключиться к базе данных')


def create_item(table_name, db_config, **data):
    db = DB(db_config)
    if db.db is not None:
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        query = f"INSERT INTO `{table_name}` ({columns}) VALUES ({placeholders})"
        params = list(data.values())
        db.execute_insert(query, params)
        print(f"Добавлены данные: {params}")

        db.db.close()
    else:
        print('Не удалось подключиться к базе данных')


def update_item(table_name, db_config, data, **conditions):
    db = DB(db_config)
    if db.db is not None:
        set_clause = ", ".join([f"{key} = %s" for key in data])
        where_clause = " AND ".join([f"{key} = %s" for key in conditions])
        query = f"UPDATE `{table_name}` SET {set_clause} WHERE {where_clause}"
        params = list(data.values()) + list(conditions.values())
        db.execute_insert(query, params)
        print(f"Обновлены данные: {data} для условий {conditions}")
        db.db.close()
    else:
        print('Не удалось подключиться к базе данных')


def create_join_query(table1, table2, db_config, type_join, join_field1, join_field2, **conditions):
    db = DB(db_config)
    if db.db is not None:
        query = (f"SELECT * FROM `{table1}` {type_join} `{table2}` ON"
                 f" `{table1}`.{join_field1} = `{table2}`.{join_field2}")
        print(query)
        if conditions:
            where_clauses = [f"{key} = %s" for key in conditions]
            query += " WHERE " + " AND ".join(where_clauses)
            print(query)
            params = list(conditions.values())
            result, columns = db.execute_query(query, params)
            formatted_result = ResultFormatter.format_result(result, columns)
            print('\n Результат JOIN-запроса:')
            for row in formatted_result:
                print(row)

        db.close_connection()
    else:
        print('Не удалось подключиться к базе данных')


def mult_join(query, params, db):
    db = DB(db)
    if db.db is not None:
        result, columns = db.execute_query(query, params)
        for row in result:
            print(row)
        db.close_connection()
    else:
        print('Соединение не установлено')


db_conf = {
        'host': 'db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
        'port': '25060',
        'user': 'st-onl',
        'passwd': 'AVNS_tegPDkI5BlB2lW5eASC',
        'database': 'st-onl'
        }

'''Сздаем студента'''
# create_item('students', db_conf, name='Виктор', second_name='Букарев')
'''Создайте несколько книг (books)'''
# create_item('books', db_conf, title='Учебник по математике 11 класс')
# create_item('books', db_conf, title='Учебник по географии 11 класс')

'''студент взял книги'''
# update_item('books', db_conf, data={'taken_by_student_id': '1945'}, id='3831')
# update_item('books', db_conf, data={'taken_by_student_id': '1945'}, id='3830')

'''Создайте группу (group)'''
# create_item('groups', db_conf, title='группа школьников 11 класс', start_date='сентябрь 2023', end_date='май 2024')

'''определите своего студента  в группу'''
# update_item('students', db_conf, data={'group_id': '1813'}, id='1945')

'''Создайте несколько учебных предметов (subjets)'''
# create_item('subjets', db_conf, title='география 11 класс')
# create_item('subjets', db_conf, title='Математика 11 класс')

'''Создайте по два занятия для каждого предмета (lessons)'''
# create_item('lessons', db_conf, title='урок математики 11 урок №1 начало в 9:00', subject_id='2545')
# create_item('lessons', db_conf, title='урок математики 11 урок №2 начало в 15:00', subject_id='2545')
# create_item('lessons', db_conf, title='урок географии 11 урок №1 начало в 16:00', subject_id='2544')
# create_item('lessons', db_conf, title='урок географии 11 урок №2 начало в 11:00', subject_id='2544')

'''Поставьте своему студенту оценки (marks) для всех созданных вами занятий'''
# create_item('marks', db_conf, value='5', lesson_id='5372', student_id='1945')
# create_item('marks', db_conf, value='5', lesson_id='5373', student_id='1945')
# create_item('marks', db_conf, value='5', lesson_id='5374', student_id='1945')
# create_item('marks', db_conf, value='5', lesson_id='5375', student_id='1945')

'''Все оценки студента'''
# create_join_query('students', 'marks', db_conf, 'RIGHT JOIN', 'id', 'value',
#                   **{'marks.student_id': '1945'})

'''Все книги, которые находятся у студента'''
# create_join_query('students', 'books', db_conf, 'RIGHT JOIN', 'id', 'title',
#                   **{'books.taken_by_student_id': '1945'})

'''Для вашего студента выведите всё, что о нем есть в базе: группа, книги, 
оценки с названиями занятий и предметов (всё одним запросом с использованием Join)'''

query = """
SELECT * 
FROM students 
JOIN `groups` ON students.group_id = `groups`.id 
JOIN books ON students.id = books.taken_by_student_id 
JOIN marks ON students.id = marks.student_id 
JOIN lessons ON students.id = marks.student_id 
JOIN subjets ON lessons.subject_id = subjets.id 
WHERE `groups`.id = %s 
  AND books.taken_by_student_id = %s 
  AND marks.student_id = %s 
  AND subjets.id = %s
"""
params = (1813, 1945, 1945, 2545)

mult_join(query, params, db_conf)
