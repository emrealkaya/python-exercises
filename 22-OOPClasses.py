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


class DogYears(object):

	year_factor = 7

	def __init__(self,age=5):
		self.age = age
		self.age_multiplied = age * self.year_factor

	def calculator(self):
		return self.age * DogYears.year_factor


my_dog = DogYears()
print(my_dog.calculator())