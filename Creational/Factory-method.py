'''Определяет интерфейс для создания объекта, но оставляет подклассам решение о том, какой класс инстанцировать.'''
class IProduct:
    def release(self):
        pass

class Car(IProduct):
    def release(self):
        pass