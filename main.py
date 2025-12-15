"""Демомодуль для курса"""


class Task:
    """Задача"""
    done: bool = False
    title: str

    def set_info(self, text: str):
        """Установка title"""
        self.title = text

    def get_info(self):
        """Получение данных задачи"""
        return self.title


task = Task()
task.set_info('Сделать лекцию')  # Установлен заголовок

print(task.get_info())  # Вывод заголовка
