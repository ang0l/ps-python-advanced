"""Демомодуль для курса
Super"""


class Order:
    """Заказ"""

    def __init__(self, number: int, total: float):
        self.number = number
        self.total = total
        print(f'Создан заказ #{number} на сумму {total}')

    def process(self):
        """Оформление заказа"""
        print('Заказ оформлен')


class EmailOrder(Order):
    """Заказ по email"""

    def __init__(self, number: int, total: float, email: str):
        super().__init__(number, total)
        self.email = email

    def process(self):
        """Оформление заказа"""
        super().process()
        print(f'Письмо отправлено на {self.email}')


e = EmailOrder(10, 1, 'a@a.ru')
e.process()
