"""Демомодуль для курса
Getattr и Setattr
"""


# class User:
#     age: float


# u = User()
# setattr(u, 'age', 10)
# print(getattr(u, 'age'))

class Commands:
    def start(self): print('Старт')
    def stop(self): print('Стоп')
    def help(self): print('Помощь')


cmd = Commands()
action = input('Введите команду > ')

if hasattr(cmd, action):
    getattr(cmd, action)()
else:
    print('Команда не найдена')
