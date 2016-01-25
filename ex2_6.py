a = range(10)
print a
print "==========xx===xx===xx============"

print "[x for x in a]"
print [x for x in a], "\n\n"

print "[x*x for x in a]"
print [x * x for x in a], "\n\n"

print "[x+1 for x in a]"
print [x + 1 for x in a], "\n\n"

print "[x for x in a if x % 2 == 0]"
print [x for x in a if x % 2 == 0], "\n\n"

print "[x*x for x in a if x % 2 == 0]"
print [x * x for x in a if x % 2 == 0], "\n\n"

p = [1, 2, 3, 4]
q = [5, 6, 7, 8]

print "[x + y for x, y in zip(p, q)]"
print [x + y for x, y in zip(p, q)], "\n\n"

print "[(x, y) for x in range(5) for y in range(5) if (x + y) % 2 == 0]"
print [(x, y) for x in range(5) for y in range(5) if (x + y) % 2 == 0], "\n\n"

print "[(x, y) for x in range(1, 6) for y in range(6, 11) if (x + y) % 2 == 0 and x != y]"
print [(x, y) for x in range(1, 6) for y in range(6, 11) if (x + y) % 2 == 0 and x != y], "\n\n"


n = 25
print "[(x, y, z) for x in range(1, n) for y in range(x, n) for z in range(y, n) if x * x + y *y == z * z]"
print [(x, y, z) for x in range(1, n) for y in range(x, n) for z in range(y, n) if x * x + y *y == z * z]

# In this exercise we've learned the list comprehensions, its
# use, its importance in python. How easily it can simplify the
# logics in a single line & easy to use. Above I execute some
# example how it can be work with lists.
