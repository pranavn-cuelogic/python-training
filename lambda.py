# Simple use of lambda
g = lambda x: x ** 2
print g(10)


def incr(n):  # Using lambda inside the function
    return lambda x: x + n

a = incr(5)
b = incr(8)

print a(40), b(52), '\n'
print incr(10)(33)

# Now using lambda with different inbuilt functions:
new_list = [2, 10, 15, 17, 24, 35, 9, 56]

print "Filter:", filter(lambda x: x % 3 == 0, new_list)  # using filter()

print "Map:", map(lambda x: x * 2 + 7, new_list)  # using map()

print "Reduce:", reduce(lambda x, y: x + y, new_list)  # using reduce()


# Function to compute prime numbers using lambda
nums = range(2, 50)
for i in range(2, 8):
    nums = filter(lambda x: x == i or x % i, nums)

print "Prime Numbers:", nums

# external mount command & to parse the output using lambda
import commands

mount = commands.getoutput('mount -v')
lines = mount.splitlines()
points = map(lambda line: line.split()[2], lines)

print points


# In this exercise we've learned the lambda function, its
# use, its importance. How it can be use with map(), filter()
# & with reduce() functions. Advantage of lambda is there is
# no need to write return it by default returns the result.
