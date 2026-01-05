"""Демомодуль для курса. Generic bound"""
from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar


class Runnable(Protocol):
    def run(self) -> None: ...


T = TypeVar('T', bound=Runnable)


@dataclass
class TaskRunner(Generic[T]):
    tasks: list[T]

    def run_all(self) -> None:
        for task in self.tasks:
            task.run()
