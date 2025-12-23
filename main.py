"""Демомодуль для курса
Упражнение - Курсы
"""

# Делаем класс Курса с ценой, названием, длительностью. Методы:
# - узнать цену
# - вывести информацию
# Делаем курс с AI и тренажерами
# - можно расчитать рассрочку на срок курса
# Делаем курс с проектом с параметром названия проекта
# - можно расчитать рассрочку на срок курса
# - можно вывести информацию о проекте


class Course:
    """Курс"""

    def __init__(self, price: float, name: str, length: int):
        self.price = price
        self.name = name
        self.length = length

    def get_price(self):
        """Получить цену"""
        return self.price

    def get_info(self):
        """Получить информацию"""
        return f'Курс {self.name} по цене {self.price} длительностью {self.length}'


class AI(Course):
    """AI и тренажеры"""

    def calc_credit(self):
        """Расчет рассрочки"""
        return self.price / self.length


class Project(Course):
    """Проект"""

    def __init__(self, price: float, name: str, length: int, project_name: str):
        super().__init__(price, name, length)
        self.project_name = project_name

    def calc_credit(self):
        """Расчет рассрочки"""
        return self.price / self.length

    def get_project_info(self):
        """Получить информацию"""
        return f'Проект: {self.project_name}'


course = Project(10000, 'Python', 2, 'Кальуклятор')
print(course.get_info())
print(course.get_project_info())
