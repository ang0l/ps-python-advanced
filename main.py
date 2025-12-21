"""Демомодуль для курса
Инкапсуляция
"""


class User:
    """Пользователь"""

    def __init__(self, name: str, balance: float):
        self.name = name
        self.__balance = balance  # __balance - приватное свойство

    def get_blance(self):
        """Получить баланс"""
        return self.__balance

    def deposit(self, amount: float):
        """Пополнить средства"""
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError('Сумма должна быть положительной')

    def withdraw(self, amount: float):
        """Снять средства"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError('Недостаточно средств')


u = User('Андрей', 1000)
u.deposit(500)
print(u.get_blance())
u.withdraw(700)
print(u.get_blance())
print(u.__dict__)

# Работа под капотом
u.__balance = -500  # не удалось изменить. создано еще одно свойство __balance
u._User__balance = -500  # удалось изменить.
print(u.get_blance())
print(u.__dict__)
