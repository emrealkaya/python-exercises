class Fruits():
	
	def __init__(self,name,calories):
		self.name = name
		self.calories = calories

	def __str__(self):
		return f"{self.name} has {self.calories}"

	def __len__(self):
		return self.calories


my_fruit = Fruits("Banane",200)

print(my_fruit)	
print(len(my_fruit))
print(str(my_fruit))