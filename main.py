"""Демомодуль для курса
Liskov Substitution Principle
"""

# Объекты дочерних классов должны быть взаимозаменяемы
# с обхектами своих базовых классов.

# Елси где-то в коде используется базовый класс,
# то можно подствить любой его наследник -
# и программа должна работать корректно, не лоамясь и не меняя поведение.

from dataclasses import dataclass


@dataclass
class User:
    name: str
    bonus: int = 0

    def add_bonus(self, amount: int):
        self.bonus += amount
        print(f'{self.name} получил {amount}. Всего {self.bonus}')


class PremiumUser(User):
    def add_bonus(self, amount: int):
        self.bonus += amount * 2
        print(f'{self.name} получил {amount}. Всего {self.bonus}')


class BannedUser(User):
    def add_bonus(self, amount: int):
        # raise Exception('Пользователь забанен')
        self.bonus = 0
        print(f'{self.name} не может получить бонусы. Всего {self.bonus}')


# user = User('Вася')

def reward_user(user: User):
    user.add_bonus(100)


reward_user(User('Вася'))
reward_user(PremiumUser('Вася'))
reward_user(BannedUser('Вася'))
