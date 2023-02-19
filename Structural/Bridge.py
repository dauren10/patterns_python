'''Структура, позволяющая изменять интерфейс обращения и интерфейс реализации класса независимо.'''
""" Code without using the bridge method
	We have a class with three attributes
	named as length, breadth, and height and
	three methods named as ProduceWithAPI1(),
	ProduceWithAPI2(), and expand(). Out of these
	producing methods are implementation-specific
	as we have two production APIs"""

'''
Метод моста — это шаблон структурного проектирования, который позволяет нам отделить абстракции, специфичные для реализации, и абстракции, независимые от реализации, друг от друга, и может разрабатываться как отдельные сущности.
Метод моста всегда считался одним из лучших методов организации иерархии классов.
     Абстракция: это ядро шаблона проектирования моста, и оно обеспечивает ссылку на разработчика.
     Усовершенствованная абстракция: она расширяет абстракцию до нового уровня, где она берет более мелкие детали на один уровень выше и скрывает более тонкие элементы от разработчиков.
     Разработчик: определяет интерфейс для классов реализации. Этот интерфейс не обязательно должен напрямую соответствовать интерфейсу абстракции и может сильно отличаться.
     Конкретная реализация: через конкретную реализацию он реализует указанный выше реализатор.
'''

class Cuboid:

	class ProducingAPI1:

		"""Implementation Specific Implementation"""

		def produceCuboid(self, length, breadth, height):

			print(f'API1 is producing Cuboid with length = {length}, '
				f' Breadth = {breadth} and Height = {height}')

	class ProducingAPI2:
		"""Implementation Specific Implementation"""

		def produceCuboid(self, length, breadth, height):
			print(f'API2 is producing Cuboid with length = {length}, '
				f' Breadth = {breadth} and Height = {height}')


	def __init__(self, length, breadth, height):

		"""Initialize the necessary attributes"""

		self._length = length
		self._breadth = breadth
		self._height = height

	def produceWithAPI1(self):

		"""Implementation specific Abstraction"""

		objectAPIone = self.ProducingAPI1()
		objectAPIone.produceCuboid(self._length, self._breadth, self._height)

	def producewithAPI2(self):

		"""Implementation specific Abstraction"""

		objectAPItwo = self.ProducingAPI2()
		objectAPItwo.produceCuboid(self._length, self._breadth, self._height)

	def expand(self, times):

		"""Implementation independent Abstraction"""

		self._length = self._length * times
		self._breadth = self._breadth * times
		self._height = self._height * times

# Instantiate a Cuboid
cuboid1 = Cuboid(1, 2, 3)

# Draw it using APIone
cuboid1.produceWithAPI1()

# Instantiate another Cuboid
cuboid2 = Cuboid(19, 20, 21)

# Draw it using APItwo
cuboid2.producewithAPI2()
