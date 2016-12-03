import sys
sys.path.append("..")
from ex48 import parser
# here there are the allowed words
directions = {'north': 'direction', 'south': 'direction', 'east': 'direction', 'west': 'direction', 'down': 'direction', 'up': 'direction', 'left': 'direction', 'right': 'direction', 'back': 'direction'}
verbs = {'go': 'verb', 'stop': 'verb', 'kill': 'verb', 'eat': 'verb'}
stops = {'the': 'stop', 'in': 'stop', 'of': 'stop', 'from': 'stop', 'at': 'stop', 'it': 'stop'}
nouns = {'door': 'noun', 'bear': 'noun', 'princess': 'noun', 'cabinet': 'noun'}
allowed_words = dict(directions)
allowed_words.update(verbs)
allowed_words.update(stops)
allowed_words.update(nouns)

def scan(words):
    result = [] # the list of tuples
    words = words.split()
    for word in words:
        # check if it is a number
        if (convert_number(word) != None):
            result.append(('number', convert_number(word)))
        # try to get the given word in the allowed_words dictionary
        elif (get_tuple(word) != None):
            #print allowed_words
            #print allowed_words.index(word)
            result.append((get_tuple(word), word))
        # word not found
        else:
            result.append(('error', word))

    print "Result: ", result
    return result

# try to convert String to int
def convert_number(word):
    try:
        return int(word)
    except ValueError:
        return None

# try to get the word in the dictionary(allowed_words)
def get_tuple(word):
    value = allowed_words.get(word, None)
    return value

sentence = raw_input("> ")
words = scan(sentence)
parser.parse_sentence(words)
