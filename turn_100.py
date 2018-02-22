from datetime import datetime

print "This program will take your age and tell you what year you will turn 100. Enjoy."
print

currentYear = datetime.now().year

go_again = True

while go_again:
	input = raw_input("Please tell me the year you were born, or your age. ")
	
	if int(input) <= 99:
		age_100 = currentYear - int(input) + 100
	
		print
		print "You are " + str(input) + " years old right now. That means you'll turn 100 in the year " + str(age_100 - 1) + " or possibly " + str(age_100) + "."
		print
	elif int(input) >= 1900:
		age_100 = int(input) + 100

		print
		print "You are " + str(currentYear - int(input)) + " years old right now. That means you'll turn 100 in the year " + str(age_100) + " or possibly " + str(age_100 + 1) + "."
		print
	else:
		print
		print "Sorry, that didn't work. Please enter the year you were born or your age."
		print
	
	again = raw_input("Would you like to try again? ")
	if again.lower() == "no" or again.lower() == "n":
		go_again = False
	else:
		print
