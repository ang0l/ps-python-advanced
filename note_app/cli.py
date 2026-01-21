"""Демомодуль для курса
Генераторы"""

from pathlib import Path
# import sys

from note_app.app import NoteManagerApp
from note_app.config.config import AppSettings


def create_app(data_path: Path | None = None):
    """Инициализация сеттингов"""

    # инизиализация settings
    settings: AppSettings

    if data_path:
        # если есть путь - устанавливается кастомный сеттинг
        settings = AppSettings.from_custom_path(data_path)
    else:
        # если пути нет - устанавливаетя дефолтный сеттинг
        settings = AppSettings.from_defaults()

    # возвращается приложение с переданными в него настройками
    return NoteManagerApp(settings)


def gen_count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1


def gen_letter():
    yield from "ABC"


def run():
    """Запуск приложения"""

    # # инициализируется переменная "путь"
    # data_path = None

    # if len(sys.argv) > 1:
    #     # если есть второй аргумент, присваивается переменной "путь"
    #     data_path = Path(sys.argv[1])

    # # пока запуск функции creat_app(data_path: Path | None = None)
    # app = create_app(data_path)
    # app.run()

    gen = gen_count_up_to(3)
    print(gen)
    print(next(gen))
    print(next(gen))
    print(next(gen))

    # number = [i for i in range(10000000)]
    number = (i for i in range(10000000))
    print(next(number))
    print(next(number))
