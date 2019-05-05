import sys

def parse_input():
    # f = sys.stdin
    with open('test.txt', 'r') as f:
        return tuple(int(x) for x in f.read().strip().split())

def run():
    n, k = parse_input()
    current = n + 1
    while(True):
        if str(current).count('5') >= k:
            print(current)
            return
        current += 1

run()
