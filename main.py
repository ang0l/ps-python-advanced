"""Демомодуль для курса
Method Resolution Order
"""


class Light:
    """Управление светом"""

    def turn_on(self):
        """Включение света"""
        print('Свет включен')


class Music:
    """Управление музыкой"""

    def turn_on(self):
        """Включение музыки"""
        print('Музыка включена')


class SmartHome(Light, Music):
    """Умный дом"""

    def play(self):
        """Включение музыки
        переопределенный метод родительского класса Music
        """
        print('Альтернативный play')

    def start(self):
        """Активация умного дома"""
        print('Умный дом активен')
        self.turn_on()
        self.play()


home = SmartHome()
home.start()

print(SmartHome.mro())
