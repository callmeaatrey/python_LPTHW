states = {
	'Delhi': 'DL',
	'Haryana': 'HR',
	'Punjab': 'PB',
	'Himachal Pradesh': 'HP',
	'Uttar Pradesh': 'UP'
}

cities = {
	'DL': 'New Delhi',
	'PB': 'Patiala',
	'UP': 'Meerut',
	'HP': 'Shimla',
	'HR': 'Sonipat'
}

# add some more cities
# cities['HP'] = 'Solan' If using this, it changes the original dict's value to Solan
cities['PB'] = 'Amritsar'

print '-' * 10
print 'All cities of Punjab: ', cities['PB']
print 'All cities of Himachal: ', cities['HP']

print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated as : %s" %(state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" %(abbrev, city)

# while doing this, make sure
print '-' * 10
for state, abbrev in states.items():
	print "%r state which is abbreviated by %r has a city named %r" %(state, abbrev, cities[abbrev])

print "-" * 10
state = states.get('Shoghi', None)

if not state:
	print "Shoghi not found!"

print "-" * 10
city = cities.get('MH', "Does not exist")

print "MH: %s" % city

