import sys

def parse_input():
    infile = sys.stdin
    # infile = open('test.txt', 'r')

    return infile.readline()[:-1]

def run():
    input = parse_input()
    alphabets = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    res = [str(input.find(x)) for x in alphabets]
    print(' '.join(res))

run()
