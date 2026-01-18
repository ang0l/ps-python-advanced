"""Модуль главного экрана"""

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header


class MainScreen(Screen):
    """Главный экран"""

    def compose(self) -> ComposeResult:

        # генерируется Header
        yield Header()
