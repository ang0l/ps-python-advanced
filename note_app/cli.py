"""Демомодуль для курса
Первый экран"""

from pathlib import Path
import sys

from note_app.config.app import NoteManagerApp
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


def run():
    """Запуск приложения"""

    # инициализируется переменная "путь"
    data_path = None

    if len(sys.argv) > 1:
        # если есть второй аргумент, присваивается переменной "путь"
        data_path = Path(sys.argv[1])

    # пока запуск функции creat_app(data_path: Path | None = None)
    app = create_app(data_path)
    app.run()
