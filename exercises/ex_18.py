print "So, which football club\'s fan do you want to become?"
print "1. Real Madrid"
print "2. FC Barcelona"

club_choice = raw_input('>')

if club_choice == '1':
	print "Good Choice. I myself chose that and here i am celebrating 4 years of fanhood!\n"
	print "Now, you gotta decide what player are you gonna tell your friends is your favorite?"
	print "1. Cristiano Ronaldo"
	print "2. Lionel Messi"

	fav_player = raw_input('>')

	if fav_player == '1':
		print "You are a true fan. Enjoy being a Madridista"
	elif fav_player == '2':
		print "What the .... ? I think you chose the wrong club before because it's not Barca , bitch!"
	else:
		print "Get the hell outta here. 404 for you!"

elif club_choice == '2':
	print "Sorry . But, you're going to be a big loser for the rest of your life.\n"

else:
	print "Incorrect Option."
