def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Let's party!!\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(16 + 33, 7 + 8)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 287, amount_of_crackers + 154)

# Extra content
print "Or even get user's input:"
new_amount_of_cheese = raw_input("Cheese: ")
new_amount_of_crackers = raw_input("Crackers: ")

cheese_and_crackers(int(new_amount_of_cheese), int(new_amount_of_crackers))
