'''Объект, который является посредником между двумя другими объектами, 
и который реализует/ограничивает доступ к объекту, к которому обращаются через него.'''
'''
Метод Proxy — это структурный шаблон проектирования, который позволяет вам обеспечить замену другого объекта. Здесь мы используем разные классы для представления функций другого класса. Самая важная часть заключается в том, что здесь мы создаем объект, имеющий исходную функциональность объекта, чтобы предоставить его внешнему миру.
Значение слова «прокси» — «вместо» или «от имени», что напрямую объясняет метод «прокси».

Прокси также называют суррогатами, дескрипторами и обертками. Они тесно связаны по структуре, но не по назначению, с адаптерами и декораторами.
Примером из реального мира может быть чек или кредитная карта, которые являются прокси того, что находится на нашем банковском счете. Он может использоваться вместо наличных денег и обеспечивает средства доступа к этим наличным деньгам, когда это необходимо. И это именно то, что делает шаблон Proxy — «Контролирует и управляет доступом к объекту, который они защищают».
Проблема без использования прокси-метода

Давайте разберемся в проблеме, рассмотрев пример базы данных колледжа, в которой хранятся все записи студентов. Например, нам нужно найти имя тех студентов из базы данных, чья плата за баланс больше 500. Итак, если мы пройдем весь список студентов и для каждого объекта студента, если мы сделаем отдельное подключение к базе данных, тогда это будет оказалось дорогостоящей задачей.
'''
class College:
	'''Resource-intensive object'''

	def studyingInCollege(self):
		print("Studying In College....")


class CollegeProxy:
	'''Relatively less resource-intensive proxy acting as middleman.
	Instantiates a College object only if there is no fee due.'''

	def __init__(self):

		self.feeBalance = 1000
		self.college = None

	def studyingInCollege(self):

		print("Proxy in action. Checking to see if the balance of student is clear or not...")
		if self.feeBalance <= 500:
			# If the balance is less than 500, let him study.
			self.college = College()
			self.college.studyingInCollege()
		else:

			# Otherwise, don't instantiate the college object.
			print("Your fee balance is greater than 500, first pay the fee")

"""main method"""

if __name__ == "__main__":
	
	# Instantiate the Proxy
	collegeProxy = CollegeProxy()
	
	# Client attempting to study in the college at the default balance of 1000.
	# Logically, since he / she cannot study with such balance,
	# there is no need to make the college object.
	collegeProxy.studyingInCollege()

	# Altering the balance of the student
	collegeProxy.feeBalance = 100
	
	# Client attempting to study in college at the balance of 100. Should succeed.
	collegeProxy.studyingInCollege()
