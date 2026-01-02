"""Демомодуль для курса. Callable"""

from typing import Callable, TypeVar


T = TypeVar('T')
R = TypeVar('R')


def process_items(items: list[T], transformer: Callable[[T], R]) -> list[R]:
    return [transformer(item) for item in items]


def to_upper(s: str) -> str:
    return s.upper()


resust = process_items(['Андрей', 'Ирина'], to_upper)

print(resust)
