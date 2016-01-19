class Parent(object):
    def implicit(self):
        print "PARENT implicit()"


class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# In this exercise we've learned how to use the implicit
# inheritance simply on parent & child class
