from sys import argv

script, user_name = argv
prompt = '> '

print "So i am %s and i am running the script called %s" % (user_name, script)
print "So , do you like me"
like = raw_input(prompt)

print "So, where do you live"
live = raw_input(prompt)

print """
So , you said %s about liking me.
You live in %s . Never heard of it.
""" % (like, live)