class Other(object):
    def override(self):
        print "Other override()"

    def implicit(self):
        print "Other implicit()"

    def altered(self):
        print "Other altered()"


class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "Child override()"

    def altered(self):
        print "Child before other altered()"
        self.other.altered()
        print "Child after other altered()"


son = Child()

son.implicit()
son.override()
son.altered()

# In this exercise we've learned how to use other classes
# & modules to access it i.e. the concept of composition
# using the Other & child class & creating the object of other class
# in child class.
