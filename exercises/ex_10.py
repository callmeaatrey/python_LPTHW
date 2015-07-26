def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" %(arg1, arg2)

def print_two_oneline(arg1, arg2):
	print "arg1: %r, arg2: %r" %(arg1, arg2)

def print_nothing():
	print "i got nothing"

print_two('Shikher', 'Aatrey')
print_two_oneline('Vidit', 'Aatrey')
print_nothing()