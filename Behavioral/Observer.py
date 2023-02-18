'''
Метод наблюдателя — это шаблон поведенческого проектирования,
 который позволяет вам определить или создать механизм подписки для отправки уведомления нескольким объектам о 
 любом новом событии, происходящем с объектом, за которым они наблюдают. Субъект в основном наблюдается несколькими объектами. 
 За субъектом необходимо следить, и всякий раз, когда в субъекте происходит изменение, наблюдатели уведомляются об этом изменении. 
 Этот шаблон определяет зависимости между объектами от одного до многих, так что один объект изменяет состояние, 
 все его зависимые объекты уведомляются и обновляются автоматически.
 
Проблема без использования метода наблюдателя

Представьте, что вы хотите создать приложение-калькулятор с различными функциями, такими как сложение, вычитание, 
изменение основания чисел на шестнадцатеричное, десятичное и многие другие функции. Но один из ваших друзей хочет изменить основу 
своего любимого числа на восьмеричную основу, а вы все еще разрабатываете приложение. Итак, какое может быть решение? 
Должен ли ваш друг проверять приложение ежедневно, просто чтобы узнать о статусе? Но не думаете ли вы, что это приведет к 
большому количеству ненужных посещений приложения, которые точно не требуются. Или вы можете думать об этом каждый раз, 
когда добавляете новую функцию и отправляете уведомление каждому пользователю. Это нормально? Иногда да, но не каждый раз. 
Возможно, некоторых пользователей обижает множество ненужных уведомлений, которые им на самом деле не нужны.
'''
class Subject:

	"""Represents what is being observed"""

	def __init__(self):

		"""create an empty observer list"""

		self._observers = []

	def notify(self, modifier = None):

		"""Alert the observers"""

		for observer in self._observers:
			if modifier != observer:
				observer.update(self)

	def attach(self, observer):

		"""If the observer is not in the list,
		append it into the list"""

		if observer not in self._observers:
			self._observers.append(observer)

	def detach(self, observer):

		"""Remove the observer from the observer list"""

		try:
			self._observers.remove(observer)
		except ValueError:
			pass



class Data(Subject):

	"""monitor the object"""

	def __init__(self, name =''):
		Subject.__init__(self)
		self.name = name
		self._data = 0

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, value):
		self._data = value
		self.notify()


class HexViewer:

	"""updates the Hexviewer"""

	def update(self, subject):
		print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))

class OctalViewer:

	"""updates the Octal viewer"""

	def update(self, subject):
		print('OctalViewer: Subject' + str(subject.name) + 'has data '+str(oct(subject.data)))


class DecimalViewer:

	"""updates the Decimal viewer"""

	def update(self, subject):
		print('DecimalViewer: Subject % s has data % d' % (subject.name, subject.data))

"""main function"""

if __name__ == "__main__":

	"""provide the data"""

	obj1 = Data('Data 1')
	obj2 = Data('Data 2')

	view1 = DecimalViewer()
	view2 = HexViewer()
	view3 = OctalViewer()

	obj1.attach(view1)
	obj1.attach(view2)
	obj1.attach(view3)

	obj2.attach(view1)
	obj2.attach(view2)
	obj2.attach(view3)

	obj1.data = 10
	obj2.data = 15
