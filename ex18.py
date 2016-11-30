# just like the previous exercises
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# script that take two arguments
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# print one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# no arguments here
def print_none():
    print "I got nothing!"

print_two("Rodrigo", "R. Galvao")
print_two_again("Rodrigo", "R. Galvao")
print_one("There we go!")
print_none()
