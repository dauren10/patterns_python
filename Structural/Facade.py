'''Объект, который абстрагирует работу с несколькими классами, объединяя их в единое целое.'''
'''
Фасадный метод — это шаблон структурного проектирования, который обеспечивает более простой унифицированный интерфейс для более сложной системы. Слово «фасад» означает лицевую сторону здания или, в частности, внешний лежащий интерфейс сложной системы, состоящей из нескольких подсистем. Это неотъемлемая часть шаблонов проектирования Gang of Four. Он обеспечивает более простой способ доступа к методам базовых систем, предоставляя единую точку входа.

'''

"""Facade pattern with an example of WashingMachine"""

class Washing:
	'''Subsystem # 1'''

	def wash(self):
		print("Washing...")


class Rinsing:
	'''Subsystem # 2'''

	def rinse(self):
		print("Rinsing...")


class Spinning:
	'''Subsystem # 3'''

	def spin(self):
		print("Spinning...")


class WashingMachine:
	'''Facade'''

	def __init__(self):
		self.washing = Washing()
		self.rinsing = Rinsing()
		self.spinning = Spinning()

	def startWashing(self):
		self.washing.wash()
		self.rinsing.rinse()
		self.spinning.spin()

""" main method """
if __name__ == "__main__":

	washingMachine = WashingMachine()
	washingMachine.startWashing()
