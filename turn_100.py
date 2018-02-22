from datetime import datetime

print "This program will take your age and tell you what year you will turn 100. Enjoy."
print

currentYear = datetime.now().year

go_again = True

while go_again:
	input = raw_input("Please tell me the year you were born, or your age. ")
	
	if int(input) <= 99:
		had_bithday = raw_input("Have you have your birthday this year? ")
		if had_bithday == "no" or had_bithday == "n":
			age_100 = currentYear - int(input) + 99
	
			print
			print "You are " + str(input) + " years old right now. That means you'll turn 100 in the year " + str(age_100) + "."
			print
		else:
			age_100 = currentYear - int(input) + 100
	
			print
			print "You are " + str(input) + " years old right now. That means you'll turn 100 in the year " + str(age_100) + "."
			print
	elif int(input) >= 1900:
		if had_bithday == "no" or had_bithday == "n":
			age_100 = int(input) + 100

			print
			print "You are " + str(currentYear - int(input) - 1) + " years old right now. That means you'll turn 100 in the year " + str(age_100) + "."
			print
		else:
			age_100 = int(input) + 100

			print
			print "You are " + str(currentYear - int(input)) + " years old right now. That means you'll turn 100 in the year " + str(age_100) + "."
			print
	else:
		if 99 < int(input) < 999:
			print
			print "What!? You are " + str(input) + " years old!? I don't think so. Please give a reasonable age - one that is below 100."
			print
		elif 1000 < int(input) < 1899:
			print
			print "What!? You are " + str(currentYear - int(input)) + " years old!? I don't think so. Please give a reasonale birth year - one that is above 1900."
			print
	
	again = raw_input("Would you like to try again? ")
	if again.lower() == "no" or again.lower() == "n":
		go_again = False
	else:
		print
