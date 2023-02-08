# class Book:
#     """ Базовый класс книги. """
#     def __init__(self, name: str, author: str):
#         self.name = name
#         self.author = author
#
#     def __str__(self):
#         return f"Книга {self.name}. Автор {self.author}"
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"
#
#
# class PaperBook:
#     def __init__(self, name: str, author: str, pages: int):
#         self.name = name
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"Книга {self.name}. Автор {self.author}"
#
#
# class AudioBook:
#     def __init__(self, name: str, author: str, duration: float):
#         self.name = name
#         self.author = author
#         self.duration = duration
#
#     def __str__(self):
#         return f"Книга {self.name}. Автор {self.author}"


class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        if not isinstance(pages, int):
            raise TypeError('Pages have to be INT format.')

        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)

        if not isinstance(duration, float):
            raise TypeError('Duration have to be FLOAT format.')

        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"