"""Модуль виджета Файлового дерева"""

from textual.containers import VerticalScroll
from textual.app import ComposeResult
from textual.widgets import Tree

from note_app.repositories import BaseFolderRerpository


class FileTreeWidget(VerticalScroll):

    _tree: Tree

    def __init__(self, folder_repo: BaseFolderRerpository, *args, **kwargs) -> None:

        self._folder_repo = folder_repo
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:

        self._tree = Tree('Заметки')

        yield self._tree
