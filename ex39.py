# working with dictionaries
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# using both dictionaries
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida gas: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and gas city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# try to get a state that is not there (safely)
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does not Exist')
print "The city for the satte 'TX' is: %s" % city
