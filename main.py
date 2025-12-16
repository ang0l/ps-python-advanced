"""Демомодуль для курса
Классовый метод
"""


class User:
    """Пользователь"""
    users = []

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        User.users.append(self)

    @classmethod
    def from_string(cls, data: str):
        """Альтернативное создание"""
        name, age = data.split(',')
        return cls(name, int(age))

    @classmethod
    def total_users(cls):
        """Число пользователей"""
        return len(cls.users)


vasia = User('Вася', 18)
kate = User('Катя', 20)
# print(vasia.total_users())
print(User.total_users())  # Правильнее будет вызвать метод так

maxim = User.from_string('Макс, 40')
print(maxim.name)
print(maxim.age)
