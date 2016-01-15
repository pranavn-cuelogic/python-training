ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = [
    "Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"
]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]  # fancy
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:6])

# In this exercise we've learned the more use of lists &
# some functions like join, split, append & pop. Adding some
# elements to list using append & displaying some elements
# using join.
