i = 0
numbers = []

while i < 4:
    print "At the tp i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now:", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

# In this exercise we've learned the while loop & its use.
# We've print the numbers till the value of i is less than 4
# & insert it into the numbers list.
