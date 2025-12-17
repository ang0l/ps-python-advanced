"""Демомодуль для курса
Dataclass
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(order=True)
class Task:
    """Задача"""
    title: str
    sectet_key: str = field(repr=False, compare=False)
    priority: int = 3
    done: bool = False
    crated_at: datetime | None = None

    def __post_init__(self):
        if self.crated_at is None:
            self.crated_at = datetime.now()


task_1 = Task('Скачать лекцию', 'mysecret')
task_2 = Task('Скачать лекцию', 'mysecret')
print(task_1)
print(task_1 == task_2)
