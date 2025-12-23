"""Демомодуль для курса
Композиция
"""
# Notification - уведомление
# EmailNotification - отправка через e-mail


class Notification:
    """Уведомление"""

    def __init__(self, sender):
        self.sender = sender

    def send(self, message):
        """Отправка"""
        self.sender.send(message)

    def get_ack(self):
        """Еще какой-нибудь метод"""


class EmailSender:
    """E-mail отправщик"""

    def send(self, message):
        """Отправление сообщения"""
        print(f'Отправлено сообщение {message}')


notification = Notification(EmailSender())
notification.send('Сообщение')
