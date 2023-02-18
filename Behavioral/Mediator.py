'''Обеспечивает взаимодействие множества объектов, формируя при этом слабую 
связанность и избавляя объекты от необходимости явно ссылаться друг на друга.

Метод медиатора — это поведенческий шаблон проектирования, который позволяет нам уменьшить неупорядоченные зависимости между объектами. 
В среде посредника объекты взаимодействуют друг с другом с помощью объектов-посредников. 
Это уменьшает связанность, уменьшая зависимости между взаимодействующими объектами. 
Посредник работает как маршрутизатор между объектами и может иметь собственную логику для обеспечения связи.
'''
class Course(object):
	"""Mediator class."""

	def displayCourse(self, user, course_name):
		print("[{}'s course ]: {}".format(user, course_name))


class User(object):
	'''A class whose instances want to interact with each other.'''

	def __init__(self, name):
		self.name = name
		self.course = Course()

	def sendCourse(self, course_name):
		self.course.displayCourse(self, course_name)

	def __str__(self):
		return self.name

"""main method"""

if __name__ == "__main__":

	mayank = User('Mayank') # user object
	lakshya = User('Lakshya') # user object
	krishna = User('Krishna') # user object

	mayank.sendCourse("Data Structures and Algorithms")
	lakshya.sendCourse("Software Development Engineer")
	krishna.sendCourse("Standard Template Library")
