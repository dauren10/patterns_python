'''Позволяет не нарушая инкапсуляцию зафиксировать 
и сохранить внутренние состояния объекта так, чтобы позднее восстановить его в этих состояниях.'''

"""Memento class for saving the data"""

"""
Memento Method — это паттерн поведенческого проектирования, который позволяет восстановить объект до его предыдущего состояния. Не раскрывая подробностей конкретных реализаций, позволяет сохранять и восстанавливать предыдущую версию объекта. Он старается не нарушать инкапсуляцию кода и позволяет захватывать и отображать внутреннее состояние объекта.
 
Проблема без использования метода Memento

Представьте, что вы студент, который хочет преуспеть в мире конкурентного программирования, 
но столкнулся с одной проблемой: найти хороший редактор кода для программирования, но ни один 
из существующих редакторов кода не соответствует вашим потребностям, поэтому вы пытаетесь сделать его для себя. 
Одной из наиболее важных функций любого редактора кода является UNDO и REDO, которые, по сути, вам также нужны. 
Как неопытный разработчик, вы просто использовали прямой подход с сохранением всех выполненных действий. 
Конечно, этот метод будет работать, но неэффективно!
"""
class Memento:

	"""Constructor function"""
	def __init__(self, file, content):

		"""put all your file content here"""
		
		self.file = file
		self.content = content

"""It's a File Writing Utility"""

class FileWriterUtility:

	"""Constructor Function"""

	def __init__(self, file):

		"""store the input file data"""
		self.file = file
		self.content = ""

	"""Write the data into the file"""

	def write(self, string):
		self.content += string

	"""save the data into the Memento"""

	def save(self):
		return Memento(self.file, self.content)

	"""UNDO feature provided"""

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content

"""CareTaker for FileWriter"""

class FileWriterCaretaker:

	"""saves the data"""

	def save(self, writer):
		self.obj = writer.save()

	"""undo the content"""

	def undo(self, writer):
		writer.undo(self.obj)


if __name__ == '__main__':

	"""create the caretaker object"""
	caretaker = FileWriterCaretaker()

	"""create the writer object"""
	writer = FileWriterUtility("GFG.txt")

	"""write data into file using writer object"""
	writer.write("First vision of GeeksforGeeks\n")
	print(writer.content + "\n\n")

	"""save the file"""
	caretaker.save(writer)

	"""again write using the writer """
	writer.write("Second vision of GeeksforGeeks\n")

	print(writer.content + "\n\n")

	"""undo the file"""
	caretaker.undo(writer)

	print(writer.content + "\n\n")
