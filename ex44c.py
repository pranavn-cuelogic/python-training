class Parent(object):
    def altered(self):
        print "PARENT altered()"


class Child(Parent):
    def altered(self):
        print"CHILD before parent altered()"
        super(Child, self).altered()
        print "CHILD, After Parent altered()"


dad = Parent()
son = Child()

dad.altered()
son.altered()

# In this exercise we've learned how to use the alter the
# parent class def in child class.
