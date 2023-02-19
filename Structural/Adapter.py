'''Объект, обеспечивающий взаимодействие двух других объектов, один из которых использует, 
а другой предоставляет несовместимый с первым интерфейс.'''
'''
Метод адаптера — это шаблон структурного проектирования, который помогает нам сделать несовместимые объекты адаптируемыми друг к другу.
 Метод адаптера — один из самых простых для понимания, потому что у нас есть много примеров из реальной жизни, которые показывают аналогию с ним. 
 Основная цель этого метода — создать мост между двумя несовместимыми интерфейсами. Этот метод предоставляет другой интерфейс для класса. 
 Нам будет легче понять эту концепцию, если подумать о кабельном адаптере, который позволяет нам заряжать телефон в любом месте с розетками разной формы. 
 Используя эту идею, мы можем интегрировать классы, которые не удалось интегрировать из-за несовместимости интерфейсов.
Проблема без использования метода адаптера

Представьте, что вы создаете приложение, которое показывает данные обо всех существующих типах транспортных средств. 
Он берет данные из API различных транспортных организаций в формате XML, а затем отображает информацию. 
Но предположим, что в какой-то момент вы захотите обновить свое приложение с помощью алгоритмов машинного обучения, которые прекрасно работают с данными и извлекают только важные данные. Но есть проблема, он принимает данные только в формате JSON. Было бы очень плохо вносить изменения в алгоритм машинного обучения, чтобы он принимал данные в формате XML.
'''
# Dog - Cycle
# human - Truck
# car - Car

class MotorCycle:

	"""Class for MotorCycle"""

	def __init__(self):
		self.name = "MotorCycle"

	def TwoWheeler(self):
		return "TwoWheeler"


class Truck:

	"""Class for Truck"""

	def __init__(self):
		self.name = "Truck"

	def EightWheeler(self):
		return "EightWheeler"


class Car:

	"""Class for Car"""

	def __init__(self):
		self.name = "Car"

	def FourWheeler(self):
		return "FourWheeler"

class Adapter:
	"""
	Adapts an object by replacing methods.
	Usage:
	motorCycle = MotorCycle()
	motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
	"""

	def __init__(self, obj, **adapted_methods):
		"""We set the adapted methods in the object's dict"""
		self.obj = obj
		self.__dict__.update(adapted_methods)

	def __getattr__(self, attr):
		"""All non-adapted calls are passed to the object"""
		return getattr(self.obj, attr)

	def original_dict(self):
		"""Print original object dict"""
		return self.obj.__dict__


""" main method """
if __name__ == "__main__":

	"""list to store objects"""
	objects = []

	motorCycle = MotorCycle()
	objects.append(Adapter(motorCycle, wheels = motorCycle.TwoWheeler))

	truck = Truck()
	objects.append(Adapter(truck, wheels = truck.EightWheeler))

	car = Car()
	objects.append(Adapter(car, wheels = car.FourWheeler))

	for obj in objects:
	    print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))
