'''Класс, который представляет собой интерфейс для создания сложного объекта.'''
'''
Метод Builder — это шаблон проектирования создания, целью которого является «отделить построение сложного объекта от его представления, чтобы один и тот же процесс построения мог создавать разные представления». Это позволяет вам строить сложные объекты шаг за шагом. Здесь, используя один и тот же код построения, мы можем легко создавать различные типы и представления объекта.
В основном он предназначен для обеспечения гибкости решений различных проблем создания объектов в объектно-ориентированном программировании.
'''
# concrete course
class DSA():

	"""Class for Data Structures and Algorithms"""

	def Fee(self):
		self.fee = 8000

	def available_batches(self):
		self.batches = 5

	def __str__(self):
		return "DSA"

# concrete course
class SDE():

	"""Class for Software development Engineer"""

	def Fee(self):
		self.fee = 10000

	def available_batches(self):
		self.batches = 4

	def __str__(self):
		return "SDE"

# concrete course
class STL():

	"""class for Standard Template Library of C++"""

	def Fee(self):
		self.fee = 5000

	def available_batches(self):
		self.batches = 7

	def __str__(self):
		return "STL"


# main method
if __name__ == "__main__":

	sde = SDE() # object for SDE
	dsa = DSA() # object for DSA
	stl = STL() # object for STL

	print(f'Name of Course: {sde} and its Fee: {sde.fee}')
	print(f'Name of Course: {stl} and its Fee: {stl.fee}')
	print(f'Name of Course: {dsa} and its Fee: {dsa.fee}')
