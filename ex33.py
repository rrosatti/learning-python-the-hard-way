numbers = []
"""
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now:", numbers
    print "At the bottom i is %d" % i
"""
def createListOfNumbers(n):
    i = 0
    while i < n:
        numbers.append(i)
        i += 1

def createListOfNumbers(n, inc):
    i = 0
    while i < n:
        numbers.append(i)
        i += inc

def printList(list):
    for element in list:
        print element


num = int(raw_input("Amount of numbers to be added: "))
changeIncrement = raw_input("Do you wanna change how much it increments? (Y or N) : ")

if changeIncrement == "Y":
    incr = int(raw_input("Increment by: "))
    createListOfNumbers(num, incr)
else:
    createListOfNumbers(num)

printList(numbers)
