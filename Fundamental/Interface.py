'''Общий метод для структурирования компьютерных программ для того, чтобы их было проще понять.
Используя комбинацию множественного наследования и абстрактных классов, вы можете использовать шаблон проектирования в Python, называемый интерфейсом. Интерфейсы — это распространенный метод объектно-ориентированного программирования, а такие языки программирования, как C# и Java, изначально реализуют эту функцию. Интерфейсы на самом деле не являются частью самого языка Python, но вы все равно можете использовать этот тип шаблона проектирования с Python. Интерфейс — это обещание или контракт, который заставляет данный класс реализовать заданное поведение.
 Сейчас мы посмотрим, как это сделать в Python.

'''
from abc import ABC, abstractmethod


class Networkdevice(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def poweron(self):
        pass


class Routify(ABC):
    @abstractmethod
    def route(self):
        pass


class Router(Networkdevice, Routify):
    def __init__(self):
        super().__init__()

    def poweron(self):
        print('Ready to process traffic')

    def route(self):
        print('Routify success')


r = Router()
r.poweron()
r.route() 
 
 
 
