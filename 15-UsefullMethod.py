
for number in list(range(20)):
	print(number*5)

print("----------------------")


for number in list(range(5,10)):
	print(number)


print("----------------------")

for number in list(range(0,21,3)):
	print(number)

print("----------------------")

index = 0

for number in list(range(5,10)):
 print(f"index: {index} number: {number}")

 index+=1

 print("----------------------")


 for  element in enumerate(list(range(5,20))):
 	print(element)


print("----------------------")

from random import randint

print(randint(0,5))

print("----------------------")

my_list = [1,2,3,4,5]

from random import shuffle

shuffle(my_list)
print(my_list)

print("----------------------")

sport_list = ["run","swim","football"]
sport_calori = [100,200,300]

zip(sport_list,sport_calori)

new_list = list(zip(sport_list,sport_calori))

print(new_list)

for element in new_list:
	print(element)

print("----------------------")


new_list = []

my_string = "emre"

for element in my_string:
	new_list.append(element)

print(new_list)

print("----------------------")

new_list = [element for element in my_string]

print(new_list)

print("----------------------")

new_list_2 = [number**3 for number in list(range(0,10))]

print(new_list_2)

print("----------------------")