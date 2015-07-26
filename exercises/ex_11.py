from sys import argv

script, filename = argv

def print_all(f):
	print f.read()

def rewind(f):
	print f.seek(0)

def print_line(line_count, f):
	print line_count, f.readline()

file_open = open(filename)

print "Let's print the whole file:\n"
print_all(file_open)

print "Lets see it all backwards:\n"
rewind(file_open)

count_line = 1
print "How about line by line:"
print_line(count_line, file_open)

count_line += 1
print_line(count_line, file_open)

count_line += 1
print_line(count_line, file_open)

print "All done!"


