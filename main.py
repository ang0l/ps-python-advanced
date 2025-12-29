"""Демомодуль для курса
Interface Segregation Principle
"""

# Клиенты не должны зависеть от методов, которые они не используют.
# Не заставляй классы реализовывать методы, которые им не нужны.

# Плохой пример
# class Printer:
#     def print_doc(self, doc: str):
#         pass

#     def scan_doc(self, doc: str):
#         pass

#     def fax_doc(self, doc: str):
#         pass


# class OldPrinter(Printer):
#     def print_doc(self, doc: str):
#         print(doc)

#     def scan_doc(self, doc: str):
#         raise NotImplementedError('Не могу')

#     def fax_doc(self, doc: str):
#         raise NotImplementedError('Не могу')


from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_doc(self, doc: str):
        pass


class Scannable(ABC):
    @abstractmethod
    def scan_doc(self, doc: str):
        pass


class Faxable(ABC):
    @abstractmethod
    def fax_doc(self, doc: str):
        pass


class ModernPrinter(Printable, Scannable, Faxable):
    def print_doc(self, doc: str):
        pass

    def scan_doc(self, doc: str):
        pass

    def fax_doc(self, doc: str):
        pass


class OldPrinter(Printable):
    def print_doc(self, doc: str):
        pass
