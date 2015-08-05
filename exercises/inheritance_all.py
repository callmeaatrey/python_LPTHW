class Parent(object):
	def altered(self):
		print "Parent Altered()"

	def implicit(self):
		print "Parent Implicit()"

	def before_after(self):
		print "Parent before_after()"

class Child(Parent):
	def altered(self):
		print "Child Altered()"

	def before_after(self):
		print "Child before_after() -before "
		super(Child, self).before_after()
		print "Child before_after() -after"

dad = Parent()
son = Child()

dad.altered()
son.altered()

print "-" * 10
dad.implicit()
son.implicit()

print "-" * 10
dad.before_after()
son.before_after()
		