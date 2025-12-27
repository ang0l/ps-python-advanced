"""Демомодуль для курса
Упражнение - Статистика учеников
"""

# Управление студентами
# У нас есть студенты с именами и оценками
# Нужно сделать возможность:
# - добавить студента в список
# - получить список студентов
# - получить среднюю оценку
# - получить лучшего студента
# - распечатать отчет - средний балл и лучший студент

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    grade: int


@dataclass
class StudentRepository:
    students: list[Student]

    def add_student(self, student: Student):
        self.students.append(student)

    def get_list_students(self) -> list[Student]:
        return self.students


@dataclass
class StaticticService:
    repository: StudentRepository

    def get_average_grade(self) -> float:
        students = self.repository.get_list_students()
        if not students:
            return 0
        total = sum(s.grade for s in students)
        return total / len(students)

    def get_best_sutdent(self) -> Student:
        students = self.repository.get_list_students()
        return max(students, key=lambda s: s.grade)


@dataclass
class ReportPrinter:
    repository: StudentRepository
    stat_service: StaticticService

    def print_report(self):
        print('Отчет по студентам')
        for s in self.repository.get_list_students():
            print(f'{s.name}: {s.grade}')
        print(f'Средний бал: {self.stat_service.get_average_grade()}')
        best = self.stat_service.get_best_sutdent()
        print(f'Лучший студент: {best.name}')


repo = StudentRepository([Student('Вася', 50)])
stat_service = StaticticService(repo)
printer = ReportPrinter(repo, stat_service)

repo.add_student(Student('Аня', 100))
repo.add_student(Student('Катя', 80))

printer.print_report()
