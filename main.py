"""Демомодуль для курса
Что такое декоратор
"""


def log_decorator(func):
    """Обертка"""
    def wrapper():
        print('Функция началась')
        func()
        print('Функция завершилась')
    return wrapper


@log_decorator
def say_hello():
    """Приветствие"""
    print('Привет!')


say_hello()
