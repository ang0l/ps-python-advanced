"""Демомодуль для курса. Упражнение - Репозиторий"""

# Нужно сделать Repository, который работает с любымим типами и имеет методы:
# add - добавляет в список элемент
# get_by_index - получает по index
# get_all - получает все

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar('T')


@dataclass
class Repository(Generic[T]):
    items: list[T]

    def add(self, item: T):
        self.items.append(item)

    def get_by_index(self, index: int) -> Optional[T]:
        if 0 <= index < len(self.items):
            return self.items[index]
        return None

    def get_all(self) -> list[T]:
        return self.items


repo = Repository[str](['a', 'b'])
print(repo.get_by_index(2))
