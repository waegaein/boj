import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [line.strip() for line in f.readlines()]

def run():
    lines = parse_input()
    for line in lines:
        if line == 'END':
            return
        else:
            print(line[::-1])

run()
