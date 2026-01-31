"""Модуль главного экрана"""

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer
from textual.containers import Horizontal

from note_app.config import AppSettings
from note_app.repositories import BaseFolderRerpository, BaseNoteRerpository
from note_app.widgets import NoteViewWidget
from note_app.widgets import FileTreeWidget


class MainScreen(Screen):
    """Главный экран"""

    CSS = """
    #tree {
        width: 25%
    }
    """

    def __init__(self, settings: AppSettings, folder_repo: BaseFolderRerpository, note_repo: BaseNoteRerpository, *args, **kwargs) -> None:

        self.settings = settings
        self._folder_repo = folder_repo
        self._note_repo = note_repo

        super().__init__(*args, **kwargs)

    BINDINGS = [
        ('q', 'quit', 'Выход'),
        ('Q', 'quit'),
        ('й', 'quit'),
        ('Й', 'quit'),
    ]

    def compose(self) -> ComposeResult:

        # генерируется Header
        yield Header()

        with Horizontal():

            # Генерируется дерево папок
            yield FileTreeWidget(self._folder_repo, self._note_repo)

            # Генерируется Маркдаун
            yield NoteViewWidget()

        # генерируется Footer
        yield Footer()

    def on_mount(self):
        self.title = 'Менеджер заметок'
        self.query_one(NoteViewWidget).text = '## Привет'

    def action_quit(self):
        self.app.exit()

    def on_file_tree_widget_note_selected(self, message: FileTreeWidget.NoteSelected) -> None:
        note = self._note_repo.load_note(message.note_path)
        if note.content:
            self.query_one(NoteViewWidget).text = note.content
        else:
            self.query_one(NoteViewWidget).text = ''
