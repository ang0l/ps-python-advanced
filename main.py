"""Демомодуль для курса
Single Responsibility Principle
"""
# Single Responsibility Principle (SRP)
# Класс должен иметь только одну причину для изменения.

from dataclasses import dataclass


@dataclass
class Order:
    items: list[str]

    def calculate_total(self):  # метод несет ответственность за заказ
        return len(self.items) * 10

    # def save_to_db(self):  # метод НЕ несет ответственность за заказ
    #     print('Сохранение в базу')

    # def send_confirmation_email(self):  # метод НЕ несет ответственность за заказ
    #     print('Отправка письма')


class OrderRepository:
    def save_to_db(self, order: Order):
        print('Сохранение в базу')


class EmailService:
    def send_confirmation_email(self, email: str, order: Order):
        print('Отправка письма')
