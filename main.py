"""Демомодуль для курса
Упражнение - Расчет скидки
"""
# Заказ в интернет магазине
# Item - name, price, qty и метод subtotal() -> считает цену
# Политики скидок - NoDiscount - без скидки, PercentageDiscount - процент от заказа
# Order - list[Item] и политика скидок, метод расчета total total_with_discount и set_policy

from dataclasses import dataclass


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
        return total * (self.percent / 100)


@dataclass
class PersentageExtraCharge:
    """Политика с наценкой"""
    percent: float

    def discount(self, total: float) -> float:
        return total * (self.percent / 100) * -1


class NoDiscount:
    """Политика без скидки"""

    def discount(self, total: float) -> float:
        return 0


class Order:
    """Заказ"""

    def __init__(self, items: list[Item], policy):
        self.items = items
        self.policy = policy

    def total(self):
        return sum(i.subtotal() for i in self.items)

    def total_with_discount(self):
        t = self.total()
        return t - self.policy.discount(t)

    def set_policy(self, policy):
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
