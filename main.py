"""Демомодуль для курса
Упражнение - Модель события"""

# Есть 3 типа событий:
# ClickEvent - x, y
# KeyEvent - key
# ResizeEvent - width, height

# Нужно сделать функцию:
# def handle_event(ev: ClickEvent | KeyEvent | ResizeEvent) -> str:
# выводит строку с параметрами события


from dataclasses import dataclass


@dataclass
class ClickEvent:
    x: int
    y: int


@dataclass
class KeyEvent:
    key: str


@dataclass
class ResizeEvent:
    width: int
    height: int


def handle_event(ev: ClickEvent | KeyEvent | ResizeEvent) -> str:
    match ev:
        case ClickEvent(x=x, y=y):
            return f'Координаты клика {x}*{y}'
        case KeyEvent(key=key):
            return f'Нажата клавиша {key}'
        case ResizeEvent(width=width, height=height):
            return f'Размер: {width}*{height}'
        case _:
            raise ValueError('Неизвестное событие')


print(handle_event(ClickEvent(1, 10)))
print(handle_event(KeyEvent('Enter')))
print(handle_event(ResizeEvent(1920, 1080)))
