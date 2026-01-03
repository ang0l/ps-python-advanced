"""Демомодуль для курса. Упражнение - Safe методы"""

# Сделать функции
# safe_get - безопасное получение элемента по индексу
# map_optional - Применяет функцию к значению, если оно не None
# or_else - Возвращает значение или default если None

from typing import Callable, Optional, TypeVar

T = TypeVar('T')
R = TypeVar('R')


def safe_get(items: list[T], index: int) -> Optional[T]:
    if 0 <= index <= len(items):
        return items[index]
    return None


def map_optional(value: Optional[T], transformer: Callable[[T], R]) -> Optional[R]:
    if value is not None:
        return transformer(value)
    return None


def or_else(value: Optional[T], default: T) -> T:
    if value is not None:
        return value
    return default
