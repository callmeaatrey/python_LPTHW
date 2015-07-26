print "How old are you, my friend?"
age = raw_input("--> ")
print "And what is your height?"
height = raw_input("--> ")
print "Sorry, but i forgot to ask you your name. What is it?"
name = raw_input("--> ")

#again we have used %r because we are still learning and trying to debug it
print "So you are %r years old and %r feets long and again i forgot to mention this, you are %r" % (age, height, name)