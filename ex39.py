# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Basic set of states & cities
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Adding more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out cities
print '=*=' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

# Print out states
print '=*=' * 10
print "Michigan abbreviation is: ", states['Michigan']
print "Florida abbreviation is: ", states['Florida']

# Using the state then cities dict
print '=*=' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# Print each state abbreviation
print '=*=' * 10
for state, abbrev in states.items():
    print "%s has the city %s" % (state, abbrev)

# Print each city in state
print '=*=' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# Now both at same time
print '=*=' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '=*=' * 10
# Get an abbreviation by state that might not there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# City with default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is: %s" % city

# In this exercise we've learned how to create dict & how to
# access the keys & values of the dict also how to access the key
# value pair form the for..loop.
