'''Представляет действие. Объект команды заключает в себе само действие и его параметры.'''
'''
Метод команды — это поведенческий шаблон проектирования, который инкапсулирует запрос в виде объекта, тем самым обеспечивая параметризацию клиентов с различными запросами, а также постановку в очередь или регистрацию запросов. Параметризация других объектов с другими запросами в нашей аналогии означает, что кнопка, используемая для включения света, может быть позже использована для включения стереосистемы или, возможно, для открытия двери гаража. Это помогает продвигать «вызов метода объекта» к полному статусу объекта. По сути, он инкапсулирует всю информацию, необходимую для выполнения действия или запуска события.
Проблема без использования командного метода

Представьте, что вы работаете над редактором кода. Ваша текущая задача — добавить новые кнопки на панель инструментов редактора для различных операций. Определенно легко создать один класс кнопок, который можно использовать для кнопок. Поскольку мы знаем, что все кнопки, используемые в редакторе, выглядят одинаково, так что же нам делать? Должны ли мы создавать множество подклассов для каждого места, где используется кнопка?
'''

"""Use built-in abc to implement Abstract classes and methods"""
from abc import ABC, abstractmethod

"""Class Dedicated to Command"""
class Command(ABC):
	
	"""constructor method"""
	def __init__(self, receiver):
		self.receiver = receiver
	
	"""process method"""
	def process(self):
		pass

"""Class dedicated to Command Implementation"""
class CommandImplementation(Command):
	
	"""constructor method"""
	def __init__(self, receiver):
		self.receiver = receiver

	"""process method"""
	def process(self):
		self.receiver.perform_action()

"""Class dedicated to Receiver"""
class Receiver:
	
	"""perform-action method"""
	def perform_action(self):
		print('Action performed in receiver.')

"""Class dedicated to Invoker"""
class Invoker:
	
	"""command method"""
	def command(self, cmd):
		self.cmd = cmd

	"""execute method"""
	def execute(self):
		self.cmd.process()

"""main method"""
if __name__ == "__main__":
	
	"""create Receiver object"""
	receiver = Receiver()
	cmd = CommandImplementation(receiver)
	invoker = Invoker()
	invoker.command(cmd)
	invoker.execute()
