my_list = [10,20,30,40,50,60]

for num in my_list:
	print(num*5)

print("----------------------")

for no in my_list:
	if no == 30:
		break
	print(no*6)

print("----------------------")


for item in my_list:
	if item ==40:
		continue
	print(item *5)

print("----------------------")