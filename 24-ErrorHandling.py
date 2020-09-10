def summation(num1,num2):
	return num1 + num2

while True:
	try:
		x = int(input("Enter first number: "))
		y = int(input("Enter second numer: "))
		
	except:
		print("Enter a number !!!")
		continue
	else:
		print(summation(x,y))
		break
		
	finally:
		pass


