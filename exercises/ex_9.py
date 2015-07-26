from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "We are going to copy the data from %r to %r." %(from_file, to_file)

# reduces the effort to write the same code in 2 lines
file1 = open(from_file)
file1_val = file1.read()
print "Number of bytes in file1 is %d " %len(file1_val)

print "Does the output file exists or not : %r " % exists(to_file)

print "Are you sure you want to do this?"
raw_input()

file2 = open(to_file, 'w')
file2.write(file1_val)

print "Alright. Done!"
file1.close()
file2.close()

