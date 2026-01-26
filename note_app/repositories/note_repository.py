"""Модуль работы с репозитория заметок"""

from pathlib import Path
from note_app.domain import Note
from note_app.repositories.base_note_repository import BaseNoteRerpository


class NoteRerpository(BaseNoteRerpository):
    """Класс Репозиторий"""

    def __init__(self, base_path: Path) -> None:

        # Преобразовываем принятый путь и сохраняем в base_path
        self.base_path = base_path.resolve()

    def _check_path(self, path: Path):
        """Проверка валидности пути"""

        if not path.exists() or not path.is_dir():
            # Если путь не существует или не является директорией: Ошибка
            raise ValueError(f'Заметка не существует: {path}')

        if self.base_path not in path.parents and path != self.base_path:
            # Если путь не внутри базового пути и не базовый путь: Ошибка
            raise ValueError('Доступ к внешнему катологу данных запрещен')

    def get_notes_by_path(self, path: Path) -> list[Note]:
        """Получение заметок"""

        # Преобразовываем принятый путь в абсолютный
        path = path.resolve()

        # Проверка валидности пути
        self._check_path(path)

        # Инициализируем пустой список для хранения папок
        notes: list[Note] = []

        # Итерация по каждому подкаталогу в выбранной директории
        for sub_path in path.iterdir():

            if sub_path.is_file() and not sub_path.name.startswith('.') and sub_path.suffix == '.md':
                # Если суб-путь - директория не начинающаяся с точки: добавляем в список
                notes.append(
                    Note(
                        name=sub_path.name,
                        path=sub_path
                    )
                )

        # Возвращае список папок отсортированный по имени
        return sorted(notes, key=lambda f: f.name)

    def create_note(self, path: Path, name: str) -> Note:
        """Создание заметок"""

        # Проверка валидности пути
        self._check_path(path)

        if not name or '/' in name or '\\' in name:
            # Если имени или в имени директории содержатся слеши: Ошибка
            raise ValueError('Неверное имя заметки')

        # Создаем директорию
        path.mkdir(parents=True, exist_ok=False)

        # Возвращаем созданную папку
        return Note(name, path)

    def delete_note(self, note: Note) -> None:
        """Удаление заметок"""
        path = note.path.resolve()

        # Проверка валидности пути
        self._check_path(path)
        path.unlink()

    def update_note(self, note: Note, content: str, new_name: str | None = None) -> Note:
        """Обновление заметки"""

        # Преобразовываем принятый путь в абсолютный
        path = note.path.resolve()

        # Проверка валидности пути
        self._check_path(path)

        path.write_text(content, encoding='utf-8')

        if new_name and new_name != note.name:
            if '/' in new_name or '\\' in new_name:
                raise ValueError('Неверное имя заметки')
            new_path = path.parent / f'{new_name}.md'
            path.rename(new_name)
            return Note(new_name, new_path)
        return note
