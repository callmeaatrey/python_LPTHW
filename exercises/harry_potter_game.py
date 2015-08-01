from sys import exit
import time
import os

def start():
	os.system('cls')
	print "In this game, you are HARRY Potter and you will be given some choices on each dialogue. \nLet\'s see where this conversation goes!"
	print "Ready?(1/0)"

	ready = raw_input('> ')
	os.system('cls')
	if ready == '1':	
		print "\nScene 1: HAGRID sees HARRY for the first when Dudley's shifts their house and decides to go live in a far away place so that they could keep HARRY away from wizards."
		time.sleep(2)
		print "\nHAGRID : I carried you in my arms when we dropped you here at these sick people\'s doorstep"
		time.sleep(2)
		print "You have got two things to say :"
		print "1. Who are you?"
		print "2. Well, you did a great job! You ruined my life. Get outta here. (Hint: Wrong Choice :P)"

		HARRY_1 = raw_input('> ')

		if HARRY_1 == '2':
			print "HAGRID : Well, looks like you became one of them. I should have never let them touch you. I think i should go. Bye!"
			exit(0)
		elif HARRY_1 == '1':
			print "HAGRID :I am HAGRID, the gatekeeper of Hogwarts. Let's go HARRY, my boy. An adventure is waiting for you"
			time.sleep(3)
			gringotts()
			os.system('cls')
		else:
			print "Wrong Choice. Play again!"
			start()

	else: 
		print "Try again"
		time.sleep(1)
		os.system('cls')
		start()

def gringotts():
	os.system('cls')
	print "Now, you are in diagon alley. You are here to buy some essential things. \n"
	print "Where do you want to go first?"
	print "1. Ollivander's (For your wand)"
	print "2. Gringotts ( to get money to buy all the things you need)"
	print "3. Pet Shop (to get yourself a pet)"
	print "4. Back to Little Whinging (because you're bored of this wizard thing)"

	harry_2 = raw_input('> ')
	money = False

	if harry_2 == '1' and money == False: 
		print "Ollivanders: I don't sell for free. Go get yourself some money first. Try Gringotts for that."
		time.sleep(2)
		os.system('cls')
		gringotts()

	elif harry_2 == '3' and money == False:
		print "Pet Shop Owner: Ohh. No money. I know you are famous , boy. But, i have a family to feed. So, go get some money first."
		print "Try Gringotts for that!"
		time.sleep(4)
		os.system('cls')
		gringotts()

	elif harry_2 == '4':
		print "You gave up too soon! Enjoy the hard life. Bye!"
		time.sleep(3)
		exit(0)

	elif harry_2 == '2':
		print "Welcome to Gringotts. I'll show you to your locker."
		money = True
		print "Try going to some shops now"
		time.sleep(3)
		os.system('cls')
		diagon_shops()

	else:
		print "Wrong choice. Choose again"
		time.sleep(3)
		os.system('cls')
		gringotts()	

	# if harry_2 == '1' and money == True:
	# 	ollivanders()

	# elif harry_2 == '3' and money == True:
	# 	pet_shop()

def diagon_shops():
	os.system('cls')
	print "Now , you have the money to buy things off your list"
	print "So, where do you want to go first?"
	print "1. Ollivanders"
	print "2. Pet Shop"

	harry_shop = raw_input('> ')

	if harry_shop == '1':
		ollivanders()
	elif harry_shop == '2':
		pet_shop()
	else:
		print "Sorry, i didn't get you.Try again"
		time.sleep(2)
		os.system('cls')
		diagon_shops()


def ollivanders():
	print "Welcome to Ollivanders"
	time.sleep(2)
	print "Here's your wand, HARRY. It has a twin and that belonged to the evil monster who killed your parents."
	time.sleep(3)
	print "His name is ..."
	time.sleep(2)
	print "Lord..."
	time.sleep(3)
	print "Lord Voldemort"
	time.sleep(2)
	print "Anyway, thanks for coming here."
	time.sleep(3)
	os.system('cls')
	print "Now, you can go to the following places: "
	print "1. Pet Shop"
	print "2. Little Whinging"

	HARRY_3 = raw_input('> ')

	if HARRY_3 == '1':
		pet_shop()

	elif HARRY_3 == '2':
		print "Well. I thought this might happen. Here's the ticket back to that hole. Bye HARRY!"
		time.sleep(2)
		exit(0)

	else:
		print "Wrong Choice ! Try again "
		os.system('cls')
		gringotts()

def pet_shop():
	os.system('cls')
	print "Hello, there. I am Madam Cruster. What kind of pet are you interested in?"
	print "1. Owl"
	print "2. Rat"
	print "3. Cat"

	HARRY_4 = raw_input('> ')

	if HARRY_4 == '1':
		print "Good Choice . here's your owl. Come again."
		time.sleep(2)
		print "HARRY: HAGRID , i think we got everything on the list. I think we should go now."
		time.sleep(3)
		print "HAGRID: OK HARRY. I'll now take you to Hogwarts. Here's your ticket to the train . "
		print "HARRY: OK"
		time.sleep(2)
		print "Thanks for playing the game! I hope you like it."
		exit(0)

	elif HARRY_4 == '2':
		print "Here's your rat. Have a good day, sir. Come again."
		time.sleep(2)
		print "HARRY: HAGRID , i think we got everything on the list. I think we should go now."
		time.sleep(3)
		print "HAGRID: OK HARRY. I'll now take you to Hogwarts. Here's your ticket to the train . "
		print "HARRY: OK"
		time.sleep(2)
		print "Thanks for playing the game! I hope you like it."
		exit(0)

	elif HARRY_4 == '3':
		print "I hope it won't bite you. Cats are magical creatures. Come again, sir."
		time.sleep(1)
		print "HARRY: HAGRID , i think we got everything on the list. I think we should go now."
		time.sleep(1)
		print "HAGRID: OK HARRY. I'll now take you to Hogwarts. Here's your ticket to the train . "
		print "HARRY: OK"
		time.sleep(1)
		print "Thanks for playing the game! I hope you like it."
		exit(0)

	else:
		print "Wrong choice. Try again !"
		pet_shop()

start()




	
