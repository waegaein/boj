import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return int(f.readline())

def get_fib(n):
    Phi = (1 + 5 ** (1 / 2)) / 2
    phi = (1 - 5 ** (1 / 2)) / 2

    return int((Phi ** n - phi ** n) / (5 ** (1 / 2)))

print(get_fib(parse_input()))
