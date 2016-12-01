def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Math, math, math..."

age = add(18, 3)
height = substract(2, 0.3)
weight = multiply(3, 20)
iq = divide(150, 3)

print "\nAge: %d\nHeight: %d\nWeight: %d\nIQ: %d" %(age, height, weight, iq)
