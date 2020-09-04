my_list = [1,2,3,4,5]

for number in my_list:
	print(number)
print("----------------------")

for num in my_list:
	if num % 2 == 0:
		print(num)

print("----------------------")
for num in my_list:
	if num == 2:
		print(num)

print("----------------------")

for item in my_list: 
	new_number = item *5
	print(new_number)

print("----------------------")

for item in my_list:
	new_number = item*5
	print(new_number)

print("----------------------")

my_string = "Emre Alkaya"

for letter in my_string:
	print(letter)
print("----------------------")

my_tuple = (1,2,3)

for item in my_tuple:
	print(item * 5)

print("----------------------")

my_new_list = [("a","b"),("c","d")]

for (x,y) in my_new_list:
	print((x,y))

print("----------------------")

my_dictionary = {"k1":100,"k2":200,"k3":300}

for(key,value) in my_dictionary.items():
	print((key,value))