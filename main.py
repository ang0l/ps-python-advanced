"""Демомодуль для курса
Упражнение - Декоратор Retry
"""

import random


def retry(times: int):
    """Декоратор Retry"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attemp in range(times):
                try:
                    return func(*args, **kwargs)
                except ValueError as e:
                    print(f'[ATTEMP {attemp + 1}]: {e}')
                    if attemp == times:
                        print('Все попытки завершены')
        return wrapper
    return decorator


@retry(3)
def unstable():
    """Иногда падает с ошибкой"""
    if random.random() < 0.7:
        raise ValueError('Ошибка соединения')

    print('Успешное выполнение')


unstable()
