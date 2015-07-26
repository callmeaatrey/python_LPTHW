from sys import argv

# script, filename = argv
# txt = open(filename)

# print "Here's your file %r" % filename
# print txt.read()

print "Type another file's name: "
txt_raw = raw_input("> ")

txt_raw_open = open(txt_raw)
print "Here's your second file %r: " % txt_raw
print txt_raw_open.read()