the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'bananas']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "this is count %d" % number

for fruit in fruits:
    print "A fruit of type %s" % fruit

for i in change:
    print "I got %r" % i

# Building the lists below
elements = []  # Empty list

# Use the range function to do 0-5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i

    # append function for insertinf in a list
    elements.append(i)

# Printing the inserted values in the list
for i in elements:
    print "The element was: %d" % i

# In this exercise we've learned the for loop & lists
# & its importance. Sometimes it require to print the output
# repetetively in that case we can use the for loop. Also
# we've created a new empty list & inserted the elements into
# it using the append & range function.
