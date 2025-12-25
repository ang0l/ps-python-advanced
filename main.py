"""Демомодуль для курса
Protocol
"""
# Заказ в интернет магазине
# Item - name, price, qty и метод subtotal() -> считает цену
# Политики скидок - NoDiscount - без скидки, PercentageDiscount - процент от заказа
# Order - list[Item] и политика скидок, метод расчета total total_with_discount и set_policy

from dataclasses import dataclass
from typing import Protocol


class DiscountPolicy(Protocol):
    """Протокол скидок"""

    def discount(self, total: float) -> float:  # type: ignore
        """Протокол скидок"""


@dataclass
class Item:
    """Единица товара"""
    name: str
    price: float
    qty: int = 1

    def subtotal(self) -> float:
        """Расчет суммы"""
        return self.price * self.qty


@dataclass
class PersentageDiscount:
    """Политика со скидкой"""
    percent: float

    def discount(self, total: float) -> float:
        """Расчет скидки"""
        return total * (self.percent / 100)


@dataclass
class PersentageExtraCharge:
    """Политика с наценкой"""
    percent: float

    def discount(self, total: float) -> float:
        """Расчет наценки"""
        return total * (self.percent / 100) * -1


class NoDiscount:
    """Политика без скидки"""

    def discount(self, total: float) -> float:
        """Расчет дискаунта"""
        return 0


@dataclass
class Order:
    """Заказ"""
    items: list[Item]
    policy: DiscountPolicy

    def total(self):
        """Стоимость по количеству"""
        return sum(i.subtotal() for i in self.items)

    def total_with_discount(self):
        """Стоимость со скидкой"""
        t = self.total()
        return t - self.policy.discount(t)

    def set_policy(self, policy):
        """Установка скидки в процентах"""
        self.policy = policy


basket = [Item('Бумага', 100, 5), Item('Ершик', 1000, 1)]
order = Order(basket, NoDiscount())
print(order.total())
print(order.total_with_discount())

order.set_policy(PersentageDiscount(10))
print(order.total())
print(order.total_with_discount())

order.set_policy(PersentageExtraCharge(10))
print(order.total())
print(order.total_with_discount())
