"""Демомодуль для курса. Union"""

from typing import Optional, TypeVar, Union

# Union - это объединение двух типов
# def safe_dif(a: float, b: float) -> Union[float, str]:


def safe_dif(a: float, b: float) -> float | str:
    if b == 0:
        return 'Деление на 0'
    return a / b


# def safe_dif2(a: float, b: float) -> float | None:
def safe_dif2(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b


T = TypeVar('T')


# def ensure_list(value: str | list[str]) -> list[str]:
def ensure_list(value: T | list[T]) -> list[T]:
    if isinstance(value, list):
        return value
    return [value]
