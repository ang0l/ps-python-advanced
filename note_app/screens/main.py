"""Модуль главного экрана"""

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer


class MainScreen(Screen):
    """Главный экран"""

    BINDINGS = [
        ('q', 'quit', 'Выход'),
        ('Q', 'quit'),
        ('й', 'quit'),
        ('Й', 'quit'),
    ]

    def compose(self) -> ComposeResult:

        # генерируется Header
        yield Header()

        # генерируется Footer
        yield Footer()

    def on_mount(self):
        self.title = 'Менеджер заметок'

    def action_quit(self):
        self.app.exit()
