"""Демомодуль для курса
Декоратор методов
"""
from functools import wraps


def log_call(fn):
    """Логирует вызов"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f'[LOG] {fn.__qualname__} args={args} kwargs={kwargs}')
        return fn(*args, **kwargs)
    return wrapper


class Service:
    """Сервиснвй"""
    @log_call
    def process(self, x: float) -> float:
        """Удваивание"""
        return x * 2


s = Service()
s.process(10)


def a():
    return 1


print(a.__name__)
print(s.process.__name__)
