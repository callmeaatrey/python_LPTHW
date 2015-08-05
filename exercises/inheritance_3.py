class Parent(object):
	def before_after(self):
		print "PARENT()"

class Child(Parent):
	def before_after(self):
		print "CHILD() before"
		super(Child, self).before_after()
		print "CHILD() after"

dad = Parent()
son = Child()

dad.before_after()
son.before_after()