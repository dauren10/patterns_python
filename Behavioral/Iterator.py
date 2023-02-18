'''Представляет собой объект, позволяющий получить последовательный доступ к 
элементам объекта-агрегата без использования описаний каждого из объектов, входящих в состав агрегации.'''
""" helper method for iterator"""


def alphabets_upto(letter):
	"""Counts by word numbers, up to a maximum of five"""
	for i in range(65, ord(letter)+1):
			yield chr(i)


"""main method"""
if __name__ == "__main__":

	alphabets_upto_K = alphabets_upto('K')
	alphabets_upto_M = alphabets_upto('M')

	for alpha in alphabets_upto_K:
		print(alpha, end=" ")

	print()

	for alpha in alphabets_upto_M:
		print(alpha, end=" ")


"""utility function"""
def inBuilt_Iterator1():
	
	alphabets = [chr(i) for i in range(65, 91)]
	
	"""using in-built iterator"""
	for alpha in alphabets:
		print(alpha, end = " ")
	print()

"""utility function"""
def inBuilt_Iterator2():
	
	alphabets = [chr(i) for i in range(97, 123)]
	
	"""using in-built iterator"""
	for alpha in alphabets:
		print(alpha, end = " ")
	print()


"""main method"""
if __name__ == "__main__" :
	
	"""call the inbuiltIterators"""
	inBuilt_Iterator1()
	inBuilt_Iterator2()
