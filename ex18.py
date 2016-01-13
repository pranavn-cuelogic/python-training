def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_one(arg1):
    print "arg1: %r" % arg1


def print_none():
    print "I got nothin'."

print_two("Pranav", "Naxane")
print_two_again("Peter", "Parker")
print_one("First!")
print_none()

# In this exercise we've learned the simple way to declare the
# function & how to use it to print the args.
