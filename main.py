"""Демомодуль для курса
Декораторы классов
"""


def add_repr(cls):
    """Добавлеине repr"""

    def __repr__(self):
        return f'{cls.__name__}[{self.__dict__}]'
    cls.__repr__ = __repr__
    return cls


@add_repr
class User:
    """Пользователь"""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


user = User('Андрей', 55)
print(user)
