# function making while takes 2 argument which tells how long will the while loop run this time and also
# about the increment factor
def while_var(range_var, increment_fctr):
	i = 0
	numbers = []
	while i < range_var:
		print "In the beginning, i is %r" %i
		numbers.append(i)
		print "Numbers list is now: ", numbers
		i += increment_fctr
		print "In the end, i is now : %r" %i
	
	print "Numbers list is: \n"

	for num in numbers:
		print num

while_var(10, 2)




