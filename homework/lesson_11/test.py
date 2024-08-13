class Book:

    reserve = bool
    availability_of_text = 'наличие текста'
    ISBN = 'Международный стандартный книжный номер'
    page_material = 'Материал страниц'

    def __init__(self, book_title, author, number_of_pages, page_material, reserve):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.reserve = reserve
        self.page_material = page_material


class SckoolBook(Book):
    home_tasks = bool

    def __init__(self, book_title, author, number_of_pages, page_material, reserve, subject, classroom):
        super().__init__(book_title, author, number_of_pages, page_material, reserve)
        self.subject = subject
        self.classroom = classroom


book1 = Book('Идиот', 'Достоевский', 500, 'Бумага', True)
book2 = Book('Идиот', 'Достоевский', 500, 'Бумага', False)
book3 = Book('Цветы для Элджернона', 'Киз', 1400, "Бумага", False)
book4 = Book('Маленький принц', 'Сент-Экзюпери', 200, "Бумага", False)
book5 = Book('Над пропастью во ржи', 'Сэлинджер', 600, "Бумага", False)


def is_true(book1):
    for item in vars(book1).items():
        if item[1] is True:
            return print(f'Название: {book1.book_title}, Автор: {book1.author}, Страниц: {book1.number_of_pages},'
                         f' Материал: {book1.page_material}, Зарезерверованно')
    else:
        return print(f'Название: {book1.book_title}, Автор: {book1.author}, Страниц: {book1.number_of_pages},'
                     f' Материал: {book1.page_material}')


scoolbook1 = SckoolBook('Алгебра', 'Иванов', '200', 'Бумага',
                        True, 'Математика', 9)
scoolbook2 = SckoolBook('Алгебра', 'Иванов', '200', 'Бумага',
                        False, 'Математика', 9)


def is_true_2(scoolbook1):
    for item in vars(scoolbook1).items():
        if item[1] is True:
            return print(f'Название: {scoolbook1.book_title}, Автор: {scoolbook1.author}, '
                         f'Страниц: {scoolbook1.number_of_pages}, Предмет: {scoolbook1.subject},'
                         f' Класс: {scoolbook1.classroom}, Зарезерверованно')
    else:
        return print(f'Название: {scoolbook1.book_title}, Автор: {scoolbook1.author},'
                     f' Страниц: {scoolbook1.number_of_pages},'
                     f' Предмет: {scoolbook1.subject}, Класс: {scoolbook1.classroom}')


is_true(book1)
is_true(book2)

is_true_2(scoolbook1)
is_true_2(scoolbook2)
