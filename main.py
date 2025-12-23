"""Демомодуль для курса
Полиморфизм
"""

len('Purple')
len([1, 2, 3])
len({1: 'a', 2: 'b'})


class Payment:
    """Оплата"""

    def pay(self, amount):
        """Метод оплаты"""
        raise NotImplementedError('Метод должен быть определен')


class CardPayment(Payment):
    """Оплата картой"""

    def pay(self, amount):
        """Метод оплаты"""
        print(f'Оплата картой: {amount}')


class CryptoPayment(Payment):
    """Оплата криптой"""

    def pay(self, amount):
        """Метод оплаты"""
        print(f'Оплата криптой: {amount}')


class ApplePayment(Payment):
    """Оплата apple"""

    def pady(self, amount):
        """Метод оплаты"""
        print(f'Оплата apple: {amount}')


payments = [CardPayment(), CryptoPayment(), ApplePayment()]

for p in payments:
    try:
        p.pay(100)
    except NotImplementedError as e:
        print(f'[Ошибка]: {e}')
