BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        self.id_ = id_
        self.name = name
        self.pages = pages

# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        self.books = books

        if self.books:
            self.id_list = [book.id_ for book in self.books]

    def get_next_book_id(self):
        if self.books:
            return self.id_list[-1] + 1
        else:
            return 1

    def get_index_by_book_id(self, id_: int):
        if id_ in self.id_list:
            return self.id_list.index(id_)
        else:
            raise ValueError('Book not found')


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
