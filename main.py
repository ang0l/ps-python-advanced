"""Демомодуль для курса
Наследование
"""


class User:
    """Пользователь платформы"""

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def get_info(self):
        return f'{self.name}, {self.email}'


class Student(User):
    """Студетн платформы"""

    def watch_video(self):
        print('Смотрю')


class Mentor(User):
    """Преподаватель платформы"""

    def check_homework(self):
        print('Проверяю')


student = Student('Вася', 'a@a.ru')
print(student.get_info())
print(student.email)
print(student.watch_video())
