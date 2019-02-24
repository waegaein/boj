import sys

def parse_input():
    infile = sys.stdin
    # infile = open('test.txt', 'r')

    return infile.readline()[:-1]

def get_occurrences(word):
    res = dict()
    for character in word.upper():
        if character in res.keys():
            res[character] += 1
        else:
            res[character] = 1
    return res

def run():
    occurrences = get_occurrences(parse_input())
    tupled = list()
    for key, value in occurrences.items():
        tupled.append((key, value))

    tupled.sort(key=lambda x: x[1], reverse=True)
    if len(tupled) > 1 and tupled[0][1] == tupled[1][1]:
        print('?')
    else:
        print(tupled[0][0])

run()
