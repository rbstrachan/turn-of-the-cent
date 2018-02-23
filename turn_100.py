from datetime import datetime

print("This program will take your age or the year you were born and tell you what year you will turn 100. Enjoy.")
print()

currentYear = datetime.now().year

go_again = True

while go_again:
	userInput = input("Please tell me your age or the year you were born. ")
	
	if 0 < int(userInput) <= 99:
		had_birthday = input("Have you have your birthday this year? ")
		if had_birthday == "no" or had_birthday == "n":
			age_100 = currentYear - int(userInput) + 99
			
			print()
			print("You are " + str(userInput) + " years old right now. That means you'll turn 100 in the year " + str(age_100) + ".")
			print()
		else:
			age_100 = currentYear - int(userInput) + 100
	
			print()
			print("You are " + str(userInput) + " years old right now. That means you'll turn 100 in the year " + str(age_100) + ".")
			print()
	elif int(currentYear - 100) <= int(userInput) <= int(currentYear - 1):
		had_birthday = input("Have you have your birthday this year? ")
		if had_birthday == "no" or had_birthday == "n":
			age_100 = int(userInput) + 100

			print()
			print("You are " + str(currentYear - int(userInput) - 1) + " years old right now. That means you'll turn 100 in the year " + str(age_100) + ".")
			print()
		else:
			age_100 = int(userInput) + 100

			print()
			print("You are " + str(currentYear - int(userInput)) + " years old right now. That means you'll turn 100 in the year " + str(age_100) + ".")
			print()
	else:
		if int(userInput) <= 0:
			print()
			print("What!? By my calulations, you are not even born yet! Please give a reasonale age - one that is above 0.")
			print()
		elif 99 < int(userInput) <= 999:
			print()
			print("What!? You are " + str(userInput) + " years old!? I don't think so. Please give a reasonable age - one that is below 100.")
			print()
		elif 1000 < int(userInput) < int(currentYear - 101):
			print()
			print("What!? You are " + str(currentYear - int(userInput)) + " years old!? I don't think so. Please give a reasonale birth year - one that is between " + str(currentYear - 100) + " and " + str(currentYear - 1) + ".")
			print()
		elif int(userInput) >= int(currentYear):
			print()
			print("What!? By my calulations, you are not even born yet! Please give a reasonale birth year - one that is between " + str(currentYear - 100) + " and " + str(currentYear - 1) + ".")
			print()
	
	again = input("Would you like to have another go? ").lower()
	if again == "no" or again == "n":
		print("See you later. Thanks for playing.")
		go_again = False
	else:
		print()
