'''Это объект, представляющий себя как уникальный экземпляр в разных местах программы, но фактически не являющийся таковым.'''
'''
Метод легковеса — это структурный шаблон проектирования, направленный на минимизацию количества объектов, которые требуются программе во время выполнения. По сути, он создает объект Flyweight, который используется несколькими контекстами. Он создан таким образом, что вы не можете отличить объект от объекта-легковеса. Одной из важных особенностей легковесных объектов является то, что они неизменяемы. Это означает, что они не могут быть изменены после того, как они были построены.
Для реализации метода Flyweight в Python мы используем Dictionary, в котором хранится ссылка на уже созданный объект, каждый объект связан с ключом.
 
Почему мы заботимся о количестве объектов в нашей программе?

 

     Меньшее количество объектов снижает использование памяти, и нам удается уберечь нас от ошибок, связанных с памятью.
     Хотя создание объекта в Python происходит очень быстро, мы все же можем сократить время выполнения нашей программы, разделяя объекты.
'''
class ComplexCars(object):

	"""Separate class for Complex Cars"""

	def __init__(self):

		pass

	def cars(self, car_name):

		return "ComplexPattern[% s]" % (car_name)


class CarFamilies(object):

	"""dictionary to store ids of the car"""

	car_family = {}

	def __new__(cls, name, car_family_id):
		try:
			id = cls.car_family[car_family_id]
		except KeyError:
			id = object.__new__(cls)
			cls.car_family[car_family_id] = id
		return id

	def set_car_info(self, car_info):

		"""set the car information"""

		cg = ComplexCars()
		self.car_info = cg.cars(car_info)

	def get_car_info(self):

		"""return the car information"""

		return (self.car_info)



if __name__ == '__main__':
	car_data = (('a', 1, 'Audi'), ('a', 2, 'Ferrari'), ('b', 1, 'Audi'))
	car_family_objects = []
	for i in car_data:
		obj = CarFamilies(i[0], i[1])
		obj.set_car_info(i[2])
		car_family_objects.append(obj)

	"""similar id's says that they are same objects """

	for i in car_family_objects:
		print("id = " + str(id(i)))
		print(i.get_car_info())
