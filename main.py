"""Демомодуль для курса. TypeGuard"""


from typing import TypeGuard


def is_int_list(x: list[int] | list[str]) -> TypeGuard[list[int]]:
    """TypeGuard
    принимает список из чисел или строк (Union)
    возвращает тип TypeGuard[list[int]]
    реально возвращает булево:
    True если список из чисел, иначе False
    """
    return all(isinstance(i, int) for i in x)


def is_str_list(x: list[int] | list[str]) -> TypeGuard[list[str]]:
    """TypeGuard
    принимает список из чисел или строк (Union)
    возвращает тип TypeGuard[list[int]]
    реально возвращает булево:
    True если список из строк, иначе False
    """
    return all(isinstance(i, str) for i in x)


def f(xs: list[int] | list[str]):
    """Применяем методы для списков из чисел и списков из строк"""
    if is_int_list(xs):  # проверяем xs на список из чисел
        xs[0].is_integer()  # можем выбрать методы только для списка из чисел
    # else:  # казалось бы, можно и так, НО...
    #     xs[0].capitalize()  # тип снова стал общим и не годен для метдоов строк

    if is_str_list(xs):  # значит проверка xs на список из строк
        xs[0].capitalize()  # теперь можем выбрать медтды для списка из строк
