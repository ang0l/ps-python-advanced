"""Демомодуль для курса
Упражнение - Методы оплат
"""
# Клиенты не должны зависеть от методов, которые они не используют.
# Не заставляй классы реализовывать методы, которые им не нужны.


from abc import ABC, abstractmethod


# class PaymentProcessor:
#     def pay(self, amount: float):
#         pass

#     def refund(self, amount: float):
#         pass

#     def tokenize_card(self, card_number: str):
#         pass

#     def check_balance(self):
#         pass


class Payable(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

    @abstractmethod
    def refund(self, amount: float):
        pass


class Tokenizable(ABC):
    @abstractmethod
    def tokenize_card(self, card_number: str):
        pass


class BalanceCheckable(ABC):
    @abstractmethod
    def check_balance(self):
        pass


class MasterCard(Payable, Tokenizable, BalanceCheckable):
    def pay(self, amount: float):
        pass

    def refund(self, amount: float):
        pass

    def tokenize_card(self, card_number: str):
        pass


class Kiwi(Payable):
    def pay(self, amount: float):
        pass

    def refund(self, amount: float):
        pass


class PayPal(Payable, BalanceCheckable):
    def pay(self, amount: float):
        pass

    def refund(self, amount: float):
        pass

    def check_balance(self):
        pass
