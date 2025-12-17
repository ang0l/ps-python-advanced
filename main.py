"""Демомодуль для курса
Property
"""


class Rectangle:
    """Прямоугольник"""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @property
    def area(self):
        """Площадь"""
        return self.width * self.height


rect = Rectangle(10, 5)

print(rect.area)  # из-за @property, теперь обращаемся к методу как к свойству
