# keywords used to do programs
# del keyword

def delete():
	a = [1, 2, 3, 4, 5, 6]
	del a[0]
	print a
	del a[2:4]
	print a
	del a[:]
	print a
	del a
	print a
}

delete()

# global keyword

def global_keyword():
	global me
	me = "Shikher Aatrey"
	print "When me is used inside this function : ", me

# using variable me outside the function to see if the global thing works
print "When printed outside the function: ", me 

# use of with keyword. the below code is commented because this is just supposed to be a dummy code

# with open('/etc/passwd', 'w') as f:
# 	f.write('Hi there!')

# assert keyword

assert 2 + 2 == 5 , "Well, this is an error!"

# pass keyword

def pass_used(): pass # this function does nothing (yet)

class c: pass # this class does nothing (yet)

# yield keyword

def create_generator():
	list_gen = range(3)
	for i in list_gen:
		yield i*i*i

mygen = create_generator()
print (mygen)

for i in mygen:
	print (i)

# class keyword

class Loaf:
	pass

# raise keyword

something_happened = True

if something_happened:
	raise "Oops. Something Happened here!"

# finally keyword

def divide_finally(a, b):
	try:
		x = a / b
	except ZeroDivisionError:
		print "Dividing by zero"
	else:
		print "result is:", x
	finally:
		print "Finally statement executed."

divide_finally(1, 0)
divide_finally(2, 1)
divide_finally(9, 2)

# lambda keyword

func = lambda x: x*x

print func(2)
print func(3)

