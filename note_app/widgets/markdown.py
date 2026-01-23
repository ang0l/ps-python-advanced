"""Модуль работы с видетом Markdown"""
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Markdown
from textual.reactive import reactive


class MarkdownWidget(VerticalScroll):
    """Клас виджета Markdown"""

    text: reactive[str | None] = reactive('')  # можно убрать типизацию

    def compose(self) -> ComposeResult:
        yield Markdown()

    def watch_text(self, _: str, new_text: str) -> None:
        self.query_one(Markdown).update(new_text)
