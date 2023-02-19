'''	Класс, расширяющий функциональность другого класса без использования наследования.'''
'''
Метод декоратора — это структурный шаблон проектирования, который позволяет вам динамически прикреплять новые поведения к объектам без изменения их реализации, помещая эти объекты внутрь объектов-оболочек, содержащих поведения.
Реализовать метод декоратора в Python гораздо проще из-за его встроенной функции. Это не эквивалентно наследованию, потому что новая функция добавляется только к этому конкретному объекту, а не ко всему подклассу.
 
Проблема без использования метода декоратора

Представьте, что мы работаем с инструментом форматирования, который предоставляет такие функции, как выделение текста жирным шрифтом и подчеркивание текста. Но через некоторое время наши инструменты форматирования стали известны среди целевой аудитории, и, получив отзывы, мы получили, что наша аудитория хочет больше функций в приложении, таких как выделение текста курсивом и многие другие функции.
Выглядит просто? Непростая задача реализовать это или расширить наши классы, чтобы добавить больше функций, не нарушая существующий клиентский код, потому что мы должны поддерживать принцип единой ответственности.
'''
class WrittenText:

	"""Represents a Written text """

	def __init__(self, text):
		self._text = text

	def render(self):
		return self._text

class UnderlineWrapper(WrittenText):

	"""Wraps a tag in <u>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<u>{}</u>".format(self._wrapped.render())

class ItalicWrapper(WrittenText):

	"""Wraps a tag in <i>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<i>{}</i>".format(self._wrapped.render())

class BoldWrapper(WrittenText):

	"""Wraps a tag in <b>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<b>{}</b>".format(self._wrapped.render())

""" main method """

if __name__ == '__main__':

	before_gfg = WrittenText("GeeksforGeeks")
	after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

	print("before :", before_gfg.render())
	print("after :", after_gfg.render())
