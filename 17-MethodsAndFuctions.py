def hello_world():
	print("hello")
	print("word")

hello_world()

print("----------------------------------")
def hello_programming(name="Python"):
	print("hello")
	print(name)


hello_programming()
"""print("----------------------------------")
def sum(number1,number2):
	number3 = number1 + number2
	print(number3)

sum(5,8)
"""
print("----------------------------------")


def summation(num1,num2,num3):
	return num1+num2+num3


my_result = summation(10,20,30)

print(my_result)


print("----------------------------------")


def control_string(s):
	if s[0] == "m":
		print(s.capitalize())

control_string("metalica")

print("----------------------------------")


def summation_2(*args):
	return sum(args)

print(summation_2(10,20))


print("----------------------------------")

def example_func(**kwargs):
	print(kwargs)

example_func(run=100,swim=200,basketball=300)
example_func(a=1,b=1)


def keyword_func(**kwargs):
	if "emre" in  kwargs:
		print("süper")
	else:
		print("değil")

keyword_func(emre=100,kemal=5,mehmet=1)