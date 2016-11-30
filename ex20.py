from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

# it will put the file in its beginning. "Address/Byte 0"
def rewind(f):
    f.seek(0)

# print the given line
def print_a_line(line_count, f):
    print line_count, f.readline()

# Extra function
def print_lines(num_of_lines, f):
    for i in range(1, num_of_lines + 1):
        print_a_line(i, f)

current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, king of like a tape."
rewind(current_file)

print "Let's print three lines:"
print_a_line(1, current_file)
print_a_line(2, current_file)
print_a_line(3, current_file)

rewind(current_file)

# Extra content
print "Now it will get more interesting:"
num_of_lines = int(raw_input("Number of lines: "))
print_lines(num_of_lines, current_file)
