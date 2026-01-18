"""Модуль создания приложения"""

from textual.app import App

from .config import AppSettings
from .screens import MainScreen


class NoteManagerApp(App):
    """Приложение Менеджер заметок"""

    def __init__(self, settings: AppSettings, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # атрибут хранения сеттинга
        self.settings = settings

    def on_mount(self) -> None:
        """Премонтирование экрана"""

        main_screen = MainScreen()
        self.push_screen(main_screen)
