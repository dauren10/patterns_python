'''	Определяет основу алгоритма и позволяет наследникам переопределять некоторые шаги алгоритма, не изменяя его структуру в целом.
Метод Template — это поведенческий шаблон проектирования, который определяет скелет операции и оставляет детали для реализации дочерним классом.
 Его подклассы могут переопределять реализацию метода по мере необходимости, но вызов должен быть таким же, как определено абстрактным классом. 
 Это один из самых простых шаблонов поведенческого проектирования для понимания и реализации. Такие методы широко используются при разработке фреймворка, 
 поскольку они позволяют нам повторно использовать один фрагмент кода в разных местах, внося определенные изменения. 
 Это также позволяет избежать дублирования кода.
 
Проблема без использования шаблонного метода

Представьте, что вы работаете над приложением чат-бота в качестве разработчика программного обеспечения, 
которое использует методы интеллектуального анализа данных для анализа данных корпоративных документов. 
Первоначально ваши приложения были в порядке только с версией данных в формате pdf, но позже вашим приложениям 
также потребуется собирать и преобразовывать данные из других форматов, таких как XML, CSV и другие. 
После реализации всего сценария и для других форматов вы заметили, что все классы имеют много похожего кода. Часть кода, такая как анализ и обработка, 
была одинаковой почти во всех классах, тогда как они различаются по работе с данными.
'''
""" method to get the text of file"""
def get_text():
	
	return "plain_text"

""" method to get the xml version of file"""
def get_xml():
	
	return "xml"

""" method to get the pdf version of file"""
def get_pdf():
	
	return "pdf"

"""method to get the csv version of file"""
def get_csv():
	
	return "csv"

"""method used to convert the data into text format"""
def convert_to_text(data):
	
	print("[CONVERT]")
	return "{} as text".format(data)

"""method used to save the data"""
def saver():
	
	print("[SAVE]")

"""helper function named as template_function"""
def template_function(getter, converter = False, to_save = False):

	"""input data from getter"""
	data = getter()
	print("Got `{}`".format(data))

	if len(data) <= 3 and converter:
		data = converter(data)
	else:
		print("Skip conversion")
	
	"""saves the data only if user want to save it"""
	if to_save:
		saver()

	print("`{}` was processed".format(data))


"""main method"""
if __name__ == "__main__":

	template_function(get_text, to_save = True)

	template_function(get_pdf, converter = convert_to_text)

	template_function(get_csv, to_save = True)

	template_function(get_xml, to_save = True)
