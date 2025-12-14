"""Демомодуль для курса"""


class User:
    """Пользоатели системы"""
    email: str
    name: str
    age: int = 39


print(type(User))

userMaria = User()
print(userMaria)

userAnton = User()
print(userAnton)

userAnton.email = 'a@a.ru'
userAnton.name = 'Антон'
# userAnton.age = 18

print(userAnton.email)
print(userAnton.age)
