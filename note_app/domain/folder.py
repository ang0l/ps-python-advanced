"""Модуль работы с папками"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Folder:
    """Класс инициализации папки"""

    name: str
    path: Path

    def __post_init__(self):
        """Пост инициализация папки"""

        if not self.name or self.name.strip() == '':
            # Если имени нет или имя пустое: Ошибка
            raise ValueError('Папка должна иметь имя')
