import sys

def parse_input():
    infile = sys.stdin
    # infile = open('test.txt', 'r')

    return infile.readline()[0]

input = parse_input()
print(ord(input))
