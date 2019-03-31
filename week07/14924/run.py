import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return tuple(int(x) for x in f.read().strip().split())

def run():
    s, t, d = parse_input()
    print(int(d / (2 * s) * t))

run()
