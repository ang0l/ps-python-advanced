"""Демомодуль для курса
Декораторы с аргументами
"""


def log(func):
    """Функция логирования"""
    def wrapper(*args, **kwargs):
        print(f'Вызов {func.__name__} с аргументами {args} {kwargs}')
        result = func(*args, **kwargs)
        print('Готово!')
        return result
    return wrapper


@log
def add(a: float, b: float) -> float:
    return a + b


print(add(3, 5))
