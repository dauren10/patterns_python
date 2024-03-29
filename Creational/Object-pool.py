'''Класс, который представляет собой интерфейс для работы с набором инициализированных и готовых к использованию объектов.
Шаблон пула объектов — это шаблон создания программного обеспечения, который используется в ситуациях, когда стоимость инициализации экземпляра класса очень высока.

По сути, пул объектов — это контейнер, который содержит некоторое количество объектов. Таким образом, когда объект берется из пула, он недоступен в пуле, пока не будет возвращен.
Объекты в пуле имеют жизненный цикл:

    Создание
    Проверка
    Разрушать.
'''
class ReusablePool:
    """
    Manage Reusable objects for use by Client objects.
    """

    def __init__(self, size):
        self._reusables = [Reusable() for _ in range(size)]

    def acquire(self):
        return self._reusables.pop()

    def release(self, reusable):
        self._reusables.append(reusable)


class Reusable:
    """
    Collaborate with other objects for a limited amount of time, then
    they are no longer needed for that collaboration.
    """

    pass


def main():
    reusable_pool = ReusablePool(10)
    reusable = reusable_pool.acquire()
    reusable_pool.release(reusable)


if __name__ == "__main__":
    main()