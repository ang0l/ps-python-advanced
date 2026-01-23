"""Модуль работы с папками репозитория"""

from pathlib import Path
from note_app.domain.folder import Folder
from note_app.repositories.base_folder_repository import BaseFolderRerpository


class FolderRerpository(BaseFolderRerpository):
    """Класс Репозиторий"""

    def __init__(self, base_path: Path) -> None:

        # Преобразовываем принятый путь и сохраняем в base_path
        self.base_path = base_path.resolve()

    def get_folders_by_path(self, path: Path) -> list[Folder]:
        """Метод формирует список папок по пути"""

        # Преобразовываем принятый путь в абсолютный
        path = path.resolve()

        if not path.exists() or not path.is_dir():
            # Если путь не существует или не является директорией: Ошибка
            raise ValueError(f'Папка не существует: {path}')

        if self.base_path not in path.parents and path != self.base_path:
            # Если путь не внутри базового пути и не базовый путь: Ошибка
            raise ValueError('Доступ к внешнему катологу данных запрещен')

        # Инициализируем пустой список для хранения папок
        folders: list[Folder] = []

        # Итерация по каждому подкаталогу в выбранной директории
        for sub_path in path.iterdir():

            if sub_path.is_dir() and not sub_path.name.startswith('.'):
                # Если суб-путь - директория не начинающаяся с точки: добавляем в список
                folders.append(
                    Folder(
                        name=sub_path.name,
                        path=sub_path
                    )
                )

        # Возвращае список папок отсортированный по имени
        return sorted(folders, key=lambda f: f.name)
