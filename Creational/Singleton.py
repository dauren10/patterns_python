'''Класс, который может иметь только один экземпляр.'''
class Singleton:
    _instance = None
    def __new__(cls):
        if not isinstance(cls._instance,cls):
            cls._instance = super().__new__(cls)
        return cls._instance

s = Singleton()
print(id(s))
print(id(s))




