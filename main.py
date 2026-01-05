"""Демомодуль для курса. Ограничения типов"""

from typing import Generic, TypeVar

Number = TypeVar('Number', int, float)  # Дженерик ограничен int-ом и float-ом


class MyMath(Generic[Number]):
    def max(self, a: Number, b: Number):
        return a if a > b else b

    def add(self, a: Number, b: Number):
        return a + b


# math = MyMath[str]()
math = MyMath[int]()
math = MyMath[float]()
