import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    raw = [line.strip() for line in f.readlines()]

    mapping = [int(num) for num in raw[0].split()]
    message = raw[1]

    return mapping, message

def get_strokes(message):
    default_mapping = {
        'a': '2', 'b': '22', 'c': '222',
        'd': '3', 'e': '33', 'f': '333',
        'g': '4', 'h': '44', 'i': '444',
        'j': '5', 'k': '55', 'l': '555',
        'm': '6', 'n': '66', 'o': '666',
        'p': '7', 'q': '77', 'r': '777', 's': '7777',
        't': '8', 'u': '88', 'v': '888',
        'w': '9', 'x': '99', 'y': '999', 'z': '9999'
    }
    strokes = list()
    for character in message:
        strokes.append(default_mapping[character])

    for i in range(len(strokes)-1):
        if strokes[i][0] == strokes[i+1][0]:
            strokes[i] += '#'

    return strokes

def parse_mapping(mapping):
    mapping_dict = dict()
    for i in range(len(mapping)):
        mapping_dict[str(mapping[i])] = str(i+1)

    return mapping_dict

def run():
    mapping, message = parse_input()
    mapping_dict = parse_mapping(mapping)
    strokes = ''.join(get_strokes(message))

    replaced = ''
    for stroke in strokes:
        if stroke == '#':
            replaced += '#'
        else:
            replaced += mapping_dict[stroke]

    print(replaced)

run()
