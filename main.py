"""Демомодуль для курса"""


class Car:
    """Машина"""
    make: str
    model: str
    year: int
    vehicle_type: str = 'Легковой'


audi = Car()
audi.make = 'Audi'
print(audi.vehicle_type)

audi.vehicle_type = 'Лодки'

Car.vehicle_type = 'Грузовой'

print(audi.vehicle_type)


class Boat:
    """Лодки"""
    # pass
    year: int


boat1 = Boat()
boat1.year = 2025
print(boat1.year)
