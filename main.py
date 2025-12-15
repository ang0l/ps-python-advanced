"""Демомодуль для курса"""

from datetime import date


class Book:
    """Книга"""

    def __init__(self, title: str, year: int) -> None:
        self.title = title
        self.year = year

    @staticmethod
    def year_since(year: int) -> int:
        return date.today().year - year


book = Book('Властелин колец', 1985)
print(Book.year_since(book.year))
