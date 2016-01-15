import hashmap

states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')


print '=*=' * 10
print "NY states has: %s" % hashmap.get(cities, 'NY')
print "OR states has: %s" % hashmap.get(cities, 'OR')

print '=*=' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

print '=*=' * 10
print ("Michigan has: %s") % hashmap.get(
    cities, hashmap.get(states, 'Michigan'))
print ("Florida has: %s") % hashmap.get(cities, hashmap.get(states, 'Florida'))

print '=*=' * 10
hashmap.list(cities)

print '=*=' * 10
state = hashmap.get(states, 'Texas')

if not state:
    print "Sorry, No Texas."

city = hashmap.get(cities, 'TX', 'Does not exist')
print "The city for the state 'TX' is: %s" % city

# In this exercise we've learned how to import the another
# file into the current file & call the functions of that file
# using it class object
