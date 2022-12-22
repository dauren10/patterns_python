class Singleton:
    def __new__(cls):
        if not  hasattr(cls,'instance'):
            cls.instance = super(Singleton,cls).__new__(cls)
        return cls.instance


s = Singleton()
s2 = Singleton()
print(id(s))
print(id(s2))