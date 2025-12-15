"""Демомодуль для курса"""


class Note:
    """Заметка"""

    # эти аргументы можно не объявлять, т.к. они создадутся в рамках инициализации
    # инициализация дает экономию на объявлении этих атрибутов
    # title: str
    # description: str
    default_description = 'Описания нет'

    def __init__(self, title: str, description: str = '') -> None:
        self.title = title
        self.description = description


note = Note('Заметка', 'Это моя заметка')
# note.title = 'Заметка'
# note.description = 'Это моя заметка'
print(note.description)

note_next = Note('Моя заметка')
