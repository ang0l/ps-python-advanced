"""Модуль создания приложения"""

from textual.app import App

from note_app.repositories import FolderRerpository, NoteRerpository


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
        folder_repo = FolderRerpository(self.settings.data_deirctory)
        note_repo = NoteRerpository(self.settings.data_deirctory)

        main_screen = MainScreen(self.settings, folder_repo, note_repo)
        self.push_screen(main_screen)
