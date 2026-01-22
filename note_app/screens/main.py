"""Модуль главного экрана"""

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Tree
from textual.containers import Horizontal

from note_app.widgets import MarkdownWidget


class MainScreen(Screen):
    """Главный экран"""

    CSS = """
    #tree {
        width: 25%
    }
    """

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
            yield Tree(label='Моя база знаний', id='tree')

            # Генерируется Маркдаун
            yield MarkdownWidget()

        # генерируется Footer
        yield Footer()

    def on_mount(self):
        self.title = 'Менеджер заметок'
        self.query_one(MarkdownWidget).text = '## Привет'

    def action_quit(self):
        self.app.exit()
