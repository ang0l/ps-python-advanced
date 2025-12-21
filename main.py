"""Демомодуль для курса
Упражнение - Декоратор limit
"""

from functools import wraps


def limit_calls(max_calls: int):
    def decorator(fn):
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            coutn_attr = f'_{fn.__name__}_count'
            current = getattr(self, coutn_attr, 0)
            if current >= max_calls:
                raise RuntimeError('Лимит запусков исчерпан')
            setattr(self, coutn_attr, current + 1)
            print(f'[LOG] {fn.__qualname__} запуск {current + 1}/{max_calls}')
            return fn(self, *args, **kwargs)
        return wrapper
    return decorator


class Engine:
    """Двигатель"""

    @limit_calls(3)
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
