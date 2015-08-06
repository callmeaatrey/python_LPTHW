class Other(object):
	def altered(self):
		print "Other altered()"
	def implicit(self):
		print "Other implicit()"
	def before_after(self):
		print "Other before_after()"
class Child(object):
	def __init__(self):
		self.other = Other()
	def altered(self):
		self.other.altered()
	def implicit(self):
		print "Child implicit()"
	def before_after(self):
		print "Child before"
		self.other.before_after()
		print "Child after"

harry = Child()

harry.altered()
print "-" * 10
harry.implicit()
print "-" * 10
harry.before_after()
