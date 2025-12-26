"""Демомодуль для курса
Упражнение - Хранилище
"""
# Хранилище
# Нужно реализовать MevoryStorage и FileStorage с методами load и save
# Приложение читает строку и передает в use_storage, сохраняет в одном из storage
# После успешного сохранения читает storage и выводит сохраненные данные

from typing import Protocol


class Storage(Protocol):
    """Протокол хранения"""

    def save(self, data: str) -> None: ...

    def load(self) -> str: ...


class MemoryStorage:
    """Хранение в памят"""

    def save(self, data: str) -> None:
        self.data = data

    def load(self) -> str:
        return getattr(self, 'data', '')


class FileStorage:
    """Хранение в памят"""

    def save(self, data: str) -> None:
        with open('data.txt', 'w', encoding='utf-8') as f:
            f.write(data)

    def load(self) -> str:
        with open('data.txt', 'r', encoding='utf-8') as f:
            return f.read()


def use_storage(storage: Storage, data: str):
    storage.save(data)
    return storage.load()


mem = MemoryStorage()
file = FileStorage()

user_input = input('Введите данные: ')
print(use_storage(mem, user_input))
print(use_storage(file, user_input))
