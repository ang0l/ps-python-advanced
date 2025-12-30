"""Демомодуль для курса
Dependency Inversion Principle
"""

# Модули верхних уровней не должны зависеть от модулей нижних уровней.
# Оба типа модулей должжны зависет от абстраций.
# Абстракции не должны зависеть от деталей.
# Детали должжнры зависет от абстракций

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Logger(ABC):
    @abstractmethod
    def log(self, message: str): ...


class FileLogger(Logger):
    def log(self, message: str):
        print(f'Запись в файл: {message}')


class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f'Запись в консоль: {message}')


@dataclass
class UserService:
    # logger = FileLogger()  # !!! Придется менять с файллоггера на консольлоггер
    logger: Logger

    def create_user(self, name: str):
        # Создает пользователя
        self.logger.log(f'Создан аккаунт {name}')


service = UserService(FileLogger())
service.create_user('Андрей')
