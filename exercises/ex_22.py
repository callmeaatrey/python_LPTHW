headmaster = "Albus Percival Wulfric Brian Dumbledore"

headmaster_split = headmaster.split(' ')

char_list = ['Harry', 'Hermione', 'Ron', 'Padfoot', 'Snape', 'Neville', 'Bellatrix', 'Scabbers']

while len(headmaster_split) != 10:
	next_one = char_list.pop()
	print "Adding: ", next_one
	headmaster_split.append(next_one)
	print "Now the length of the list is %r" %len(headmaster_split)

print "There we go: ", headmaster_split

print "Let\'s do something with this list: "

print headmaster_split[1]
print headmaster_split[-1]
print ' '.join(headmaster_split) 
print '#'.join(headmaster_split[3:5])