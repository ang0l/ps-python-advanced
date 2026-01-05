"""Демомодуль для курса. Упражнение - Поиск по id"""

# Есть User, Product и Order у которых есть поле id.
# Нужно сделать универвальную функицю поиска по id


from dataclasses import dataclass
from typing import Optional, Protocol, TypeVar


class Identifiable(Protocol):
    id: int


T = TypeVar('T', bound=Identifiable)


@dataclass
class User:
    id: int
    name: str
    email: str


@dataclass
class Product:
    id: int
    title: str


@dataclass
class Order:
    id: int
    products: list[Product]


def get_by_id(items: list[T], id_: int) -> Optional[T]:
    for item in items:
        # проверка на id
        if item.id == id_:
            return item
        return None


get_by_id([User(1, 'Андрей', 'a@a.ru')], 1)
