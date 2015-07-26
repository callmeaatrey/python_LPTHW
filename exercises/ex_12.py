def jelly_count(start_count):
	jelly_belly = start_count * 100
	eat_me = jelly_belly / 10
	return jelly_belly, eat_me

count, eat = jelly_count(100)

print "1. %r \n2. %r \n" %(count, eat)

print "a. %r \nb. %r" %jelly_count(100)

print "All done!"