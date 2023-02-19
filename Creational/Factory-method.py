'''Фабричный метод — это порождающий шаблон проектирования, который позволяет интерфейсу или классу создавать объект, но позволяет подклассам решать, какой класс или объект создавать. Используя метод Factory, у нас есть лучшие способы создания объекта. Здесь объекты создаются без раскрытия логики клиенту, а для создания нового типа объекта клиент использует тот же общий интерфейс.
 
Проблемы, с которыми мы сталкиваемся без Factory Method:

Представьте, что у вас есть собственный стартап, который занимается райдшерингом в разных уголках страны. Первоначальная версия приложения обеспечивает только совместное использование двухколесных транспортных средств, но со временем ваше приложение становится популярным, и теперь вы хотите добавить также совместное использование трех- и четырехколесных транспортных средств.
Это отличная новость! а как насчет разработчиков программного обеспечения вашего стартапа. Им приходится менять весь код, потому что теперь большая часть кода связана с классом Two-Wheeler, и разработчикам приходится вносить изменения во всю кодовую базу.
После внесения всех этих изменений разработчики заканчивают работу либо с грязным кодом, либо с заявлением об увольнении.'''
# Python Code for Object
# Oriented Concepts without
# using Factory method

class FrenchLocalizer:

	""" it simply returns the french version """

	def __init__(self):

		self.translations = {"car": "voiture", "bike": "bicyclette",
							"cycle":"cyclette"}

	def localize(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class SpanishLocalizer:
	"""it simply returns the spanish version"""

	def __init__(self):

		self.translations = {"car": "coche", "bike": "bicicleta",
							"cycle":"ciclo"}

	def localize(self, msg):

		"""change the message using translations"""
		return self.translations.get(msg, msg)

class EnglishLocalizer:
	"""Simply return the same message"""

	def localize(self, msg):
		return msg

if __name__ == "__main__":

	# main method to call others
	f = FrenchLocalizer()
	e = EnglishLocalizer()
	s = SpanishLocalizer()

	# list of strings
	message = ["car", "bike", "cycle"]

	for msg in message:
		print(f.localize(msg))
		print(e.localize(msg))
		print(s.localize(msg))
