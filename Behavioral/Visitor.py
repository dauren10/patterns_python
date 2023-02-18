'''Описывает операцию, которая выполняется над объектами других классов. 
При изменении класса Visitor нет необходимости изменять обслуживаемые классы.'''
'''
""" Иерархия курсов не может быть изменена для добавления новых
функциональность динамически. Абстрактный класс Crop для
Конкретные классы Courses_At_GFG: методы, определенные в этом классе
будет унаследован всеми классами Concrete Courses_At_GFG."""

класс Courses_At_GFG:

def принять (я, посетитель):
посетитель. посетите (я)

def обучение (я, посетитель):
print(self, "Учил", посетитель)

def изучение(самостоятельно, посетитель):
print(я, "изучает", посетитель)


защита __str__(я):
вернуть себя.__класс__.__имя__


"""Concrete Courses_At_GFG class: Посещаемые классы."""
класс SDE(Courses_At_GFG): пройти

класс STL (Courses_At_GFG): пройти

класс DSA (Courses_At_GFG): успешно


""" Класс Abstract Visitor для классов Concrete Visitor:
метод, определенный в этом классе, будет унаследован всеми
Конкретные классы для посетителей."""
Посетитель класса:

защита __str__(я):
вернуть себя.__класс__.__имя__


""" Бетонные посетители: Классы посещают объекты Бетонного курса.
Эти классы имеют метод visit(), который вызывается
Метод accept() классов Concrete Course_At_GFG."""
Инструктор класса (Посетитель):
визит по определению (я, урожай):
обрезать.обучение(самостоятельно)


Класс Студент(Посетитель):
визит по определению (я, урожай):
урожай.обучение(самостоятельно)


"""создание объектов для конкретных классов"""
СДЭ = СДЭ()
СТЛ = СТЛ()
ДСА = ДСА()

"""Создание посетителей"""
инструктор = инструктор()
студент = студент ()

"""Посетители курсов"""
sde.accept(инструктор)
sde.accept(студент)

stl.accept(инструктор)
stl.accept(студент)

dsa.accept(инструктор)
dsa.accept(ученик)'''

""" The Courses hierarchy cannot be changed to add new
functionality dynamically. Abstract Crop class for
Concrete Courses_At_GFG classes: methods defined in this class
will be inherited by all Concrete Courses_At_GFG classes.


"""

class Courses_At_GFG:

	def accept(self, visitor):
		visitor.visit(self)

	def teaching(self, visitor):
		print(self, "Taught by ", visitor)

	def studying(self, visitor):
		print(self, "studied by ", visitor)


	def __str__(self):
		return self.__class__.__name__


"""Concrete Courses_At_GFG class: Classes being visited."""
class SDE(Courses_At_GFG): pass

class STL(Courses_At_GFG): pass

class DSA(Courses_At_GFG): pass


""" Abstract Visitor class for Concrete Visitor classes:
method defined in this class will be inherited by all
Concrete Visitor classes."""
class Visitor:

	def __str__(self):
		return self.__class__.__name__


""" Concrete Visitors: Classes visiting Concrete Course objects.
These classes have a visit() method which is called by the
accept() method of the Concrete Course_At_GFG classes."""
class Instructor(Visitor):
	def visit(self, crop):
		crop.teaching(self)


class Student(Visitor):
	def visit(self, crop):
		crop.studying(self)


"""creating objects for concrete classes"""
sde = SDE()
stl = STL()
dsa = DSA()

"""Creating Visitors"""
instructor = Instructor()
student = Student()

"""Visitors visiting courses"""
sde.accept(instructor)
sde.accept(student)

stl.accept(instructor)
stl.accept(student)

dsa.accept(instructor)
dsa.accept(student)
