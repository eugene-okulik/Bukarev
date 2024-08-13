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

    def __str__(self):
        if self.reserve:
            return (f"Название: {self.book_title}, Автор: {self.author}, "
                    f"страниц: {self.number_of_pages}, материал: {self.page_material}, зарезервирована")
        else:
            return (f"Название: {self.book_title}, Автор: {self.author}, "
                    f"страниц: {self.number_of_pages}, материал: {self.page_material}")


class SckoolBook(Book):
    home_tasks = bool

    def __init__(self, book_title, author, number_of_pages, page_material, reserve, subject, classroom):
        super().__init__(book_title, author, number_of_pages, page_material, reserve)
        self.subject = subject
        self.classroom = classroom

    def __str__(self):
        if self.reserve:
            return (f"Название: {self.book_title}, Автор: {self.author}, "
                    f"страниц: {self.number_of_pages}, Предмет: {self.subject},"
                    f" Класс: {self.classroom}, зарезервирована")
        else:
            return (f"Название: {self.book_title}, Автор: {self.author}, "
                    f"страниц: {self.number_of_pages}, Предмет: {self.subject}, Класс: {self.classroom}")


book1 = Book('Идиот', 'Достоевский', 500, 'Бумага', True)
book2 = Book('Идиот', 'Достоевский', 500, 'Бумага', False)
book3 = Book('Цветы для Элджернона', 'Киз', 1400, "Бумага", False)
book4 = Book('Маленький принц', 'Сент-Экзюпери', 200, "Бумага", False)
book5 = Book('Над пропастью во ржи', 'Сэлинджер', 600, "Бумага", False)

print(book1)
print(book2)

scoolbook1 = SckoolBook('Алгебра', 'Иванов', '200', 'Бумага',
                        True, 'Математика', 9)
scoolbook2 = SckoolBook('Алгебра', 'Иванов', '200', 'Бумага',
                        False, 'Математика', 9)
print(scoolbook1)
print(scoolbook2)
