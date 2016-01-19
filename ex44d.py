class Parent(object):
    def override(self):
        print "Parent override()"

    def implicit(self):
        print "Parent implicit()"

    def altered(self):
        print "Parent altered()"


class Child(Parent):
    def override(self):
        print "Child override() access zali"

    def altered(self):
        print "Child before parent altered()"
        super(Child, self).altered()
        print "Child after parent altered()"


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

# In this exercise we've combined all three types of
# inheritance (i.e. Implicit, override & altered) & call them
# to check whether they execute properly or not.
