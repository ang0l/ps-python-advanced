"""Демомодуль для курса
Упражнение - Декоратор limit
"""

from functools import wraps
from typing import Any


class Limit:
    def __init__(self, count: int):
        self.count = count

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*arg, **kwarg):
            if self.count <= 0:
                raise RuntimeError('Визов лимита исчерпан')
            self.count -= 1
            return fn(*arg, **kwarg)
        return wrapper
# def limit_calls(max_calls: int):
#     def decorator(fn):
#         @wraps(fn)
#         def wrapper(self, *args, **kwargs):
#             coutn_attr = f'_{fn.__name__}_count'
#             current = getattr(self, coutn_attr, 0)
#             if current >= max_calls:
#                 raise RuntimeError('Визов лимита исчерпан')
#             setattr(self, coutn_attr, current + 1)
#             print(f'[LOG] {fn.__qualname__} запуск {current + 1}/{max_calls}')
#             return fn(self, *args, **kwargs)
#         return wrapper
#     return decorator


class Engine:
    """Двигатель"""

    # @limit_calls(3)
    @Limit(3)
    def start(self):
        """Запуск"""
        print('Двигатель запущен!')


car = Engine()

try:
    car.start()
    car.start()
    car.start()
    car.start()  # <-- Ошибка Runtime Error
except RuntimeError as e:
    print(f'[ERROR]: {e}')
