import sys
from math import gcd

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [[int(x) for x in line.split()] for line in f.read().strip().split('\n')[1:]]

def get_order(M, N, x, y):
    total = abs(M * N) // gcd(M, N)

    while x <= total:
        if (x - y) % N == 0:
            return x
        else:
            x += M

    return -1

def main():
    cases = parse_input()

    for case in cases:
        print(get_order(*case))

    return

main()
