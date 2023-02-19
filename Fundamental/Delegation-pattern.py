"""Объект внешне выражает некоторое поведение, но в реальности передаёт ответственность 
за выполнение этого поведения связанному объекту.

Шаблон делегирования — это шаблон объектно-ориентированного проектирования, который позволяет композиции объектов добиться того же повторного использования кода, что и наследование». 
Если вы прочитаете это предложение четыре или пять раз, вы можете понять его, но позвольте мне попытаться упростить его.
"""
class Animal:
  def __init__(self, name, num_of_legs):
    self.name = name
    self.num_of_legs = num_of_legs
  
  def get_number_of_legs(self):
    print(f"I have {self.num_of_legs} legs")

class Dog(Animal):
  def __init__(self, name, num_of_legs):
    super().__init__(name, num_of_legs)

dog = Dog('Fido', 4)
dog.get_number_of_legs()

# Outputs "I have 4 legs"