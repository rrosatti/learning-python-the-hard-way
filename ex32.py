the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'bananas', 'strawberries']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "This is a count %d" % number

for fruit in fruits:
    print "Fruit: %s" % fruit

for i in change:
    print "I got %r" % i

# building a list

elements = []

for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)

for e in elements:
    print "Element: %d" % e
