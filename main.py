"""Демомодуль для курса
Встроенные методы
"""


class ShoppingList:
    """Список покупок"""

    def __init__(self, items: list[str]) -> None:
        self.items: list[str] = items

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, ShoppingList):
            return False
        return self.items == value.items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __repr__(self) -> str:
        # return f'[{', '.join(self.items)}]'
        return f'ShoppingList[items = {', '.join(self.items)}]'


list_1 = ShoppingList(['Книга'])
list_2 = ShoppingList(['Телевизор', 'Компьютер'])

print(len(list_1))
print(list_1[0])
print(list_2[1])
print(list_2)

print(list_1 == list_2)
