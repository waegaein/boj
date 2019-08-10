import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return tuple(int(num) for num in f.readline().strip().split())

def run():
    res = 1
    n, m  = parse_input()
    for i in range(n, n-m, -1):
        res *= i
    for i in range(1, m+1):
        res //= i

    print(res)

run()
