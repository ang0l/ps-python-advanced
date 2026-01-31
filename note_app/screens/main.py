"""Модуль главного экрана"""

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer
from textual.containers import Horizontal

from note_app.config import AppSettings
from note_app.repositories import FolderRerpository, NoteRerpository
from note_app.widgets import NoteViewWidget
from note_app.widgets import FileTreeWidget


class MainScreen(Screen):
    """Главный экран"""

    CSS = """
    #tree {
        width: 25%
    }
    """

    def __init__(self, settings: AppSettings, *args, **kwargs) -> None:

        self.settings = settings

        super().__init__(*args, **kwargs)

    BINDINGS = [
        ('q', 'quit', 'Выход'),
        ('Q', 'quit'),
        ('й', 'quit'),
        ('Й', 'quit'),
    ]

    def compose(self) -> ComposeResult:

        folder_repo = FolderRerpository(self.settings.data_deirctory)
        note_repo = NoteRerpository(self.settings.data_deirctory)
        # генерируется Header
        yield Header()

        with Horizontal():

            # Генерируется дерево папок
            yield FileTreeWidget(folder_repo, note_repo)

            # Генерируется Маркдаун
            yield NoteViewWidget()

        # генерируется Footer
        yield Footer()

    def on_mount(self):
        self.title = 'Менеджер заметок'
        self.query_one(NoteViewWidget).text = '## Привет'

    def action_quit(self):
        self.app.exit()
