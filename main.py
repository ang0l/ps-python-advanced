"""Демомодуль для курса
Упражнение - Уведомления
"""

# Принцип открытости и закрытости
# Классы должны быть открыты для расшинения, но закрыты для модификации


from abc import ABC, abstractmethod
from dataclasses import dataclass


# class Notifier:
#     def send(self, message: str, method: str) -> None:
#         if method == 'email':
#             print(f'[Email] Отправлено сообщение: {message}')
#         elif method == 'push':
#             print(f'[Push] Отправлено сообщение: {message}')
#         else:
#             print('Неизвестный способ уведомлелния')

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f'[Email] Отправлено сообщение: {message}')


class PushNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f'[Push] Отправлено сообщение: {message}')


class TelegramNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f'[Telegram] Отправлено сообщение: {message}')


@dataclass
class NotificationService:
    notifier: Notifier

    def send(self, message: str):
        self.notifier.send(message)


service = NotificationService(TelegramNotifier())
service.send('Привет')
