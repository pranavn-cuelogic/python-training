def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b


def substract(a, b):
    print "substracting %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "multiplying %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "dividing %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

val1 = int(raw_input("Enter first value: "))
val2 = float(raw_input("Enter second value: "))

age = add(val1, val2)
height = substract(val1, val2)
weight = multiply(val1, val2)
iq = divide(val1, val2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (
    age, height, weight, iq
)

# Puzzle for the extra credit.
print "\n\nHere is a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# In this exercise we've learned the use of return in a
# function & some math operation, also we have seen how we
# can directly assign function to a variable to get return
# result. The another tricky way to write a function.
