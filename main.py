"""Демомодуль для курса. Упражнение - Оповещения о низком остатке"""

# Сделать LowStockService, который в мтоде run() проверяет в
# InMemoryStockRepository - сколько осталось товара (число items)
# и если их меньше 10 - отправляется уведомление через EmailNotifier

from dataclasses import dataclass
from typing import Protocol


class StockRepository(Protocol):
    def get_stock_count(self) -> int: ...


class Notifier(Protocol):
    def notify(self, message: str): ...


@dataclass
class InMemoryStockRepository:
    items_count: int

    def get_stock_count(self) -> int:
        return self.items_count


class EmailNotifier:
    def notify(self, message: str):
        print(f'email - {message}')


@dataclass
class LowStockService:
    repository: StockRepository
    notifier: Notifier

    def run(self):
        if self.repository.get_stock_count() <= 10:
            self.notifier.notify('Мало товара')
        else:
            print('Проверка пройдена')


service = LowStockService(InMemoryStockRepository(12), EmailNotifier())
service.run()
