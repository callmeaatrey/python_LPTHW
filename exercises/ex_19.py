# for loops

clubs = ['RM', 'FCB', 'MU', 'MC']
players = ['CR7', 'LM10', 'ISCO', 'OZIL']
managers = ['Benitez', 'Mourinho', 'Guardiola']

for i in clubs:
	print "I like %r" %i

for i in players:
	print "My favorite player is %r" %i

for i in managers:
	print "My club is managed by %r" %i


raw = []

for i in range(0,6):
	print "I just added %r to the list!" %i
	raw.append(i)

for i in raw:
	print "Well, this is %r , which i just added to the list" %i


raw_2 = []

# how to make 2d lists (multiple)
for i in range(0,2):
	raw_2.append([clubs]+[players])

for i in raw_2:
	print "%r" %i


	
