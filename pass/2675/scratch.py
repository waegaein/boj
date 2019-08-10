import sys

def parse_input():
    input = sys.stdin
    # input = open('test.txt', 'r')
    input.readline()
    res = list()
    for line in input.readlines():
        splitted = line.split()
        res.append((int(splitted[0]), splitted[1]))

    return(res)

def multiply(factor, word):
    return ''.join([character * factor for character in word])

def run():
    inputs = parse_input()
    for input in inputs:
        print(multiply(*input))

    return

run()
