"""Демомодуль для курса
Дескриптор
"""


class Positive:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, owner):
        print('Сработал get')
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        print('Сработал set')
        if value <= 0:
            raise ValueError(
                f'Значение "{self.name}" должно быть больше нуля. Ваше значение = {value}')
        obj.__dict__[self.name] = value


class Product:
    price = Positive('price')


p = Product()
p.price = 100
print(p.price)
try:
    p.price = -1
except ValueError as e:
    print(f'[Error]: {e}')
