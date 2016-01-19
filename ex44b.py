class Parent(object):
    def override(self):
        print "PARENT override()"


class Child(Parent):
    def override(self):
        print "CHILD override()"


dad = Parent()
son = Child()

dad.override()
son.override()

# In this exercise we've learned how to use the override
# the def function in parent class, in child class
