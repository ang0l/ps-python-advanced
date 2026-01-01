"""Демомодуль для курса. Slots"""


from dataclasses import dataclass
import sys


class A:
    def __init__(self) -> None:
        self.x = 1
        self.y = 1


print(A.__dict__)

a = A()


class B:
    __slots__ = ('x', 'y')

    def __init__(self) -> None:
        self.x = 1
        self.y = 1


b = B()
print(b.x)
print(b.y)
# b.z = 1

print(sys.getsizeof(a))
print(sys.getsizeof(a.__dict__))
print(sys.getsizeof(b))


@dataclass(slots=True)
class Point:
    x: int
    y: int


p = Point(1, 1)


class D3Point(Point):
    __slots__ = ('z',)


class MyPoint(Point):
    pass


p2 = MyPoint(1, 2)
print(p2.__dict__)
