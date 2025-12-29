"""Демомодуль для курса
Упражнение - Оплата в рассрочку
"""

# Создать 3 метода платежа:
# - Всю сумму
# - Всю сумму - число бонусов
# - Деление на N частей, 1 сразу, остальные потом


from dataclasses import dataclass


class Payment:
    def pay(self, amount: float) -> float:
        print(f'Списано: {amount}')
        return amount


@dataclass
class BonusPayment(Payment):
    bonuses: float = 0

    def pay(self, amount: float) -> float:
        final = amount - self.bonuses
        print(f'Списано: {final}')
        return final


@dataclass
class InstallmentPayment(Payment):
    part: int = 0

    def pay(self, amount: float) -> float:
        final = amount / self.part
        print(f'Списано: {final}')
        return final


def pay(method: Payment):
    return method.pay(100)


pay(InstallmentPayment(2))
pay(BonusPayment(25))
