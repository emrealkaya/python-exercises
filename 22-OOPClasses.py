class Musician():

	job = "Musician"
	def __init__(self,name,age,instrument):
		self.name = name
		self.age = age
		self.instrument = instrument
	def sing(self):
		print(f"We are champions! {self.instrument}")

my_musician = Musician("Emre",24,"Guitar")
print(my_musician.age)
print(my_musician.name)
print(my_musician.instrument)
print(my_musician.job)
my_musician.sing()

print("-----------------")
class DogYears(object):

	year_factor = 7

	def __init__(self,age=5):
		self.age = age
		self.age_multiplied = age * self.year_factor

	def calculator(self):
		return self.age * DogYears.year_factor


my_dog = DogYears()
print(my_dog.calculator())

print("-----------------")
##inheritance

class Class1():
	def __init__(self):
		print("Class 1 created")

	def method1(self):
		print("method 1")

	def  method2(self):
		print("method2")

class Class2(Class1):

	def __init__(self):
		Class1.__init__(self)
		print("Claas 2 created")
	def method2(self):
		print("its overiding")


my_instance_1=Class2()
print(my_instance_1)
print(my_instance_1.method2())

print("-----------------")

class Apple():
	def __init__(self,name):
		self.name = name
	def information(self):
		return self.name + "100 calories"


class Banana():
	def __init__(self,name):
		self.name = name
	def information(self):
		return self.name + "200 calories"

banana = Banana("banana")
apple = Apple("apple")

my_fruit_list = [banana,apple]

for fruit in my_fruit_list:
	print(fruit.information())


def get_info(fruit):
	print(fruit.information())


print(get_info(banana))