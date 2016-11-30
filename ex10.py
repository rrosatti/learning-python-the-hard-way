# -*- coding: utf-8 -*-
my_name = "Rodrigo R. Galvao"
my_age = 21
my_height = 1.71
my_weight = 58.50

print "If I add %d, %.2f, and %.2f I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "What is this -> %r" % (my_name + " " + str(21))

#advanced printing
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat
