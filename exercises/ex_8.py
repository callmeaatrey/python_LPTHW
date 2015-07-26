from sys import argv 

script, filename = argv

print "I will be deleting file %r" % filename
print "If you want to cancel it, use the keys CTRL + C!"
print "IF not, press ENTER!"

raw_input('?')

print "Let's open a newfile"
file_open = open(filename, 'w')

print "Let's truncate this bitch. Goodbye"
file_open.truncate()

print "Ready to build the file again"

line1 = raw_input('1.')
line2 = raw_input('2.')
line3 = raw_input('3.')

print "Ready to write these files to the file"


# You can use file_open.writelines([line1, line2, line3])
# or using formats file_open.write("%s \n %s \n %s \n" ) % (line1, line2, line3)
file_open.write(line1)
file_open.write('\n')
file_open.write(line2)
file_open.write('\n')
file_open.write(line3)
file_open.write('\n')

# print "Wanna take a look at what you did. Here it is.... "

# print file_open.read()

file_open.close()

