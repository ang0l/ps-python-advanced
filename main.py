"""Демомодуль для курса"""

# Герой, у которого есть имя, hp, inventory list и пометка жив ли он
# Нужно сделать методы take_damage, heal, add_item, show_status


class Hero:
    """Герой игры"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.hp: int = 100
        self.inventory: list[str] = []
        self.status = True

    def take_damage(self, damage: int):
        """Получение урона"""
        if not self.status:
            print(f'{self.name} уже повержен')
            return
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.status = False
            print(f'{self.name} теперь повержен')
        else:
            print(f'{self.name} получил {damage} урона')

    def heal(self, heal: int):
        """Лечение"""
        if not self.status:
            print(f'{self.name} уже повержен')
            return
        self.hp = min(self.hp + heal, 100)
        print(f'{self.name} восстановил {heal} HP. Текущие HP {self.hp}')

    def add_item(self, item: str):
        """Инвентарь"""
        self.inventory.append(item)
        print(f'{self.name} получил предмет {item}')

    def show_status(self):
        """Показ статуса"""
        status = 'Жив' if self.status else 'Повержен'
        print(
            f'{self.name} - HP: {self.hp}. Инвентарь: {self.inventory}. [{status}]')


hero = Hero('Андрей')
hero.add_item('Мечь')
hero.show_status()
hero.take_damage(30)
hero.take_damage(60)
hero.heal(50)
hero.show_status()
hero.take_damage(65)
hero.show_status()
hero.take_damage(10)
