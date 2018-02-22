from datetime import datetime

print "This program will take your age and tell you what year you will turn 100. Enjoy."
print

currentYear = datetime.now().year

go_again = True

while go_again:
	age = raw_input("How old are you? ")
	age_100 = currentYear - int(age) + 100

	print
	print "You are " + str(age) + " years old right now. That means you'll turn 100 in the year " + str(age_100) + " or possibly " + str(age_100 + 1) + "."
	print
	
	again = raw_input("Would you like to try again? ")
	if again.lower() == "no" or again.lower() == "n":
		go_again = False
	else:
		print
