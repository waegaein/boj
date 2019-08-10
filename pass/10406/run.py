import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return tuple([int(x) for x in line.split()] for line in f.read().strip().split('\n'))

def run():
    input = parse_input()
    w = input[0][0]
    n = input[0][1]
    p = input[0][2]
    punches = input[1]
    count = 0
    for punch in punches:
        if punch >= w and punch <= n:
            count += 1
    print(count)

run()
