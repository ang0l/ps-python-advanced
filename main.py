"""Демомодуль для курса. Упражнение - Работа с tuple"""

# make_pair - создаёт Tuple из двух значений
# get_first - достаёт первый элемент из пары
# get_second - достаёт второй элемент из пары
# swap_pair - меняет элементы местами

from typing import TypeVar


T = TypeVar('T')
R = TypeVar('R')


def make_pair(a: T, b: R) -> tuple[T, R]:
    return (a, b)


def get_first(pair: tuple[T, R]) -> T:
    return pair[0]


def get_second(pair: tuple[T, R]) -> R:
    return pair[1]


def swap_pair(pair: tuple[T, R]) -> tuple[R, T]:
    return (pair[1], pair[0])
