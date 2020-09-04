name = input("Name: ")
print("Welcome " + name + " time to play hangman!")

secret_word = "besiktas"

guess_string = ""

count = 8

while count > 0:

	character_left = 0

	for character in secret_word:

		if character in guess_string:

			print(character)
		else:
			print("-")
			character_left += 1

	if character_left == 0:
		print("You won!!!")	
		break


	guess = input("Guess a word: ")
	guess_string += guess

	if guess not in secret_word:
		count -= 1
		print("Wrong!")
		print(f"You have {count} left")

		if count == 0:
			print("You died!")